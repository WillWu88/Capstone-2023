import numpy as np
import rclpy
from math import cos, sin, pi, degrees
from rclpy.node import Node
from std_msgs.msg import String, Header
from sensor_msgs.msg import Imu
from tutorial_interfaces.msg import GPS, PoseSetpoint, RPM, VelSetpoint, XFiltered, Heading
from message_filters import ApproximateTimeSynchronizer, Subscriber
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
from drivers.kf_constants import *
from drivers.car_param import *
from drivers.gps_helper import *

class KalmanNode(Node):

    def __init__(self):
        super().__init__('kalman_filter_x')
        self.state_pub = self.create_publisher(XFiltered, 'x_filtered', 10) 

        self.heading_sub = self.create_subscription(Heading, 'heading', self.heading_update, 10)
        self.heading = 0.

        # x-axis kf config
        self.f_s = 100.0
        self.kf_x = KalmanFilter(dim_x=2, dim_z=2)
        self.kf_x.x = np.array([[0.0],[0.0]])
        self.discrete_b = np.array([[1./(self.f_s*self.f_s*2.), 1./(self.f_s*self.f_s*2.)],
                               [1./self.f_s, 1./self.f_s]])

        x_b = np.array([[cos(self.heading*pi), sin(self.heading*pi)],
                        [cos(self.heading*pi), sin(self.heading*pi)]])
        y_b = np.array([[-sin(self.heading*pi), cos(self.heading*pi)],
                        [-sin(self.heading*pi), cos(self.heading*pi)]])
        self.kf_init(self.kf_x, self.f_s, np.array([[1, 0],[0, 1]]),
                     ms_var * np.array([[gps_x_var, 0.], [0., ms_var]]),
                     Q_mult_x * Q_discrete_white_noise(2, 1./self.f_s, var=imu_x_var),
                     custom_B=np.multiply(x_b, self.discrete_b))

        # x-axis kf config
        self.f_s = 100.0
        self.kf_y = KalmanFilter(dim_x=2, dim_z=2)
        self.kf_y.x = np.array([[0.0],[0.0]])
        self.kf_init(self.kf_y, self.f_s, np.array([[1., 0.], [0., 1.]]),
                     R_mult_y * np.array([[gps_y_var, 0.],[0. ms_var]]),
                     Q_mult_y * Q_discrete_white_noise(2, 1./self.f_s, var=imu_y_var),
                     custom_B=np.multiply(y_b, self.discrete_b))
        self.kf_y.inv = np.reciprocal


        self.imu_sub = Subscriber(self, Imu, "/imu_raw", qos_profile=10) #qos profile always 10
        self.rpm_sub = Subscriber(self, RPM, "/rpm_raw", qos_profile=10) 
        # time synchronizer
        self.time_sync = ApproximateTimeSynchronizer([self.imu_sub, self.rpm_sub], 
                                                     10, 
                                                     0.01)

        self.time_sync.registerCallback(self.kf_update)

        # GPS fusion, expand after normal kf
        self.gps_sub = self.create_subscription(GPS, 'gps_raw', self.gps_callback, 10)
        self.update_not_used = True # potential race condition?
        self.gps_x = 0.
        self.gps_y = 0.

    def kf_init(self, kf, f_s, custom_H, custom_R, 
                custom_Q, custom_F=None, custom_B=None):
        '''default: dt double integrator F=ma process 
            initial covariance set to identity
        '''
        if custom_F is None:
            kf.F = np.array([[1., 1./f_s],[0., 1.]])
        else:
            kf.F = custom_F
        if custom_B is None:
            kf.B = np.array([[1./(f_s*f_s*2.)],[1./f_s]]) # imu input
        else:
            kf.B = custom_B
        kf.H = custom_H
        kf.R = custom_R
        kf.Q = custom_Q

    def kf_update(self, imu_msg, rpm_msg):
        self.get_logger().info('Kalman updating')
        try:
            assert imu_msg.header.stamp == rpm_msg.header.stamp
        except AssertionError:
            self.get_logger().info("Time stamp mismatch")
        finally:
            u_x = imu_msg.linear_acceleration.x - imu_x_mean
            u_y = imu_msg.linear_acceleration.y - imu_y_mean
            process_meas = np.array([[u_x], [u_y]])

            self.kf_x.predict(u=process_meas)
            self.kf_x.predict(u=process_meas)
            vel_meas = rpm_msg.derivedms - ms_mean

            # gps fusion, update with GPS if coordinate is available
            if (self.update_not_used):
                self.get_logger().info('Updating with GPS')
                x_pos_meas = approx_distance(origin_x, self.gps_x)
                y_pos_meas = approx_distance(origin_y, self.gps_y)
                self.update_not_used = False
            else: 
                # use previous state estimate if not available
                x_pos_meas = float(self.kf_x.x[0])
                y_pos_meas = float(self.kf_y.x[0])
            

            x_meas = np.array([[x_pos_meas],[vel_meas*cos(self.heading*pi)]])
            y_meas = np.array([[y_pos_meas],[vel_meas*sin(self.heading*pi)]])

            self.kf_x.update(x_meas)
            self.kf_y.update(y_meas)
            x_msg = XFiltered()
            x_msg.header.stamp = self.get_clock().now().to_msg()
            x_msg.header.frame_id = 'mixed' 
            x_msg.xpos = float(self.kf_x.x[0])
            x_msg.xvel = float(self.kf_x.x[1])
            x_msg.ypos = float(self.kf_y.x[0])
            x_msg.yvel = float(self.kf_y.x[1])
            x_msg.xbvel = float(frame_transfer_x(self.heading, 
                                                            self.kf_x.x[1], 
                                                            self.kf_y.x[1]))
            x_msg.ybvel = float(frame_transfer_y(self.heading, 
                                                            self.kf_x.x[1], 
                                                            self.kf_y.x[1]))
            self.state_pub.publish(x_msg)
            
            
            self.get_logger().info('Kalman X Updated')

    def gps_callback(self, gps_msg):
        self.update_not_used = True;
        # get new gps reading
        new_x = math.copysign(gps_msg.latmin, gps_msg.latdeg) # north-south, latitude
        new_y = math.copysign(gps_msg.longmin, gps_msg.longdeg) # east-west, longitude

        # update distance measurement, correct for bias
        self.gps_x = new_x - gps_x_mean
        self.gps_y = new_y - gps_y_mean

    def heading_update(self, heading_msg):
        self.heading = heading_msg.heading
        x_b = np.array([[cos(self.heading*pi), sin(self.heading*pi)],
                        [cos(self.heading*pi), sin(self.heading*pi)]])
        y_b = np.array([[-sin(self.heading*pi), cos(self.heading*pi)],
                        [-sin(self.heading*pi), cos(self.heading*pi)]])
        self.kf_x.B = np.multiply(x_b, self.discrete_b)
        self.kf_y.B = np.multiply(y_b, self.discrete_b)

        

def main(args=None):
    rclpy.init(args=args)

    kalman = KalmanNode()

    rclpy.spin(kalman)

    #rpm_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()


