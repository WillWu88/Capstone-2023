import numpy as np
import rclpy
from math import cos, sin, pi
from rclpy.node import Node
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

        self.f_s = 100.0
        # local frame linear kalman filter for speed tracking
        self.kf_localx = KalmanFilter(dim_x=1, dim_z=1)
        self.kf_localx.x = np.array([[0.0]])
        self.kf_init(self.kf_localx, self.f_s, np.array([[1.]]), 
                     local_ms_mult * ms_var, local_imu_x_mult * imu_x_var,
                     custom_F = np.array([[1.]]), custom_B=np.array([[1./self.f_s]]))

        # x-axis kf config
        self.kf_x = KalmanFilter(dim_x=2, dim_z=2)
        self.kf_x.x = np.array([[0.0],[0.0]])
        self.discrete_b = np.array([[1./(self.f_s*self.f_s*2.)],
                                   [1./self.f_s]])

        x_b = np.array([[cos(self.heading*pi), sin(self.heading*pi)]])
        y_b = np.array([[-sin(self.heading*pi), cos(self.heading*pi)]])
        self.kf_init(self.kf_x, self.f_s, np.array([[1, 0],[0, 1]]),
                     R_mult_x * np.array([[gps_x_var, 0.], [0., ms_var * ms_x_mult]]),
                     Q_mult_x * Q_discrete_white_noise(2, 1./self.f_s, var=imu_x_var),
                     custom_B=np.dot(self.discrete_b, x_b))

        # y-axis kf config
        self.kf_y = KalmanFilter(dim_x=2, dim_z=2)
        self.kf_y.x = np.array([[0.0],[0.0]])
        self.kf_init(self.kf_y, self.f_s, np.array([[1., 0.], [0., 1.]]),
                     R_mult_y * np.array([[gps_y_var, 0.],[0., ms_var * ms_y_mult]]),
                     Q_mult_y * Q_discrete_white_noise(2, 1./self.f_s, var=imu_y_var),
                     custom_B=np.dot(self.discrete_b, y_b))

        # time synchronizer for simultaneous sensor reading
        self.imu_sub = Subscriber(self, Imu, "/imu_raw", qos_profile=10) #qos profile always 10
        self.rpm_sub = Subscriber(self, RPM, "/rpm_raw", qos_profile=10) 
        self.time_sync = ApproximateTimeSynchronizer([self.imu_sub, self.rpm_sub],
                                                     10, 
                                                     0.01)

        self.time_sync.registerCallback(self.kf_update)

        # GPS Fusion
        self.gps_sub = self.create_subscription(GPS, 'gps_raw', self.gps_callback, 10)
        self.update_not_used = True # potential race condition?
        self.ORIGIN_X = 64.8417 #north-south direction, latitude
        self.ORIGIN_Y = -30.2358 #east west-direction, longitude
        self.gps_x = self.ORIGIN_X
        self.gps_y = self.ORIGIN_Y

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
        # self.get_logger().info('Kalman updating')
        try:
            assert imu_msg.header.stamp == rpm_msg.header.stamp
        except AssertionError:
            # self.get_logger().info("Time stamp mismatch")
            pass
        finally:
            u_x = imu_msg.linear_acceleration.x - imu_x_mean
            u_y = imu_msg.linear_acceleration.y - imu_y_mean
            process_meas = np.array([[u_x], [u_y]])

            self.kf_x.predict(u=process_meas)
            self.kf_y.predict(u=process_meas)
            self.kf_localx.predict(u=u_x)
            vel_meas = rpm_msg.derivedms - ms_mean

            # gps fusion, update with GPS if coordinate is available
            if (self.update_not_used):
                self.get_logger().warning('Updating with GPS')
                x_pos_meas = approx_distance_lat(self.ORIGIN_X, self.gps_x)
                y_pos_meas = approx_distance_lon(self.ORIGIN_Y, self.gps_y)
                self.update_not_used = False
            else: 
                self.get_logger().warning('Updating without GPS')
                # use previous state estimate if not available
                x_pos_meas = float(self.kf_x.x[0])
                y_pos_meas = float(self.kf_y.x[0])

            x_meas = np.array([[x_pos_meas], [vel_meas*cos(self.heading*pi)]])
            y_meas = np.array([[y_pos_meas], [vel_meas*sin(self.heading*pi)]])

            self.kf_x.update(x_meas)
            self.kf_y.update(y_meas)
            self.kf_localx.update(vel_meas)
            x_msg = XFiltered()
            x_msg.header.stamp = self.get_clock().now().to_msg()
            x_msg.header.frame_id = 'mixed' 
            x_msg.xpos = float(self.kf_x.x[0])
            x_msg.xvel = float(self.kf_x.x[1])
            x_msg.ypos = float(self.kf_y.x[0])
            x_msg.yvel = float(self.kf_y.x[1])
            x_msg.xbvel = float(self.kf_localx.x[0])
            x_msg.ybvel = float(frame_transfer_y(self.heading, 
                                                            self.kf_x.x[1], 
                                                            self.kf_y.x[1]))
            x_msg.debug_gps_x = self.gps_x
            x_msg.debug_gps_y = self.gps_y
            x_msg.debug_gps_x_org = x_pos_meas
            x_msg.debug_gps_y_org = y_pos_meas
            self.state_pub.publish(x_msg)
            
            
            # self.get_logger().info('Kalman X Updated')

    def gps_callback(self, gps_msg):
        self.get_logger().warning('Updating GPS')
        # if (gps_msg.latmin < 63 or gps_msg.longmin > -29):
        #     self.get_logger().warning('Removing Outlier')
        #     # remove outliers
        #     return 
        # else:
        self.update_not_used = True;
        # get new gps reading
        new_x = math.copysign(gps_msg.latmin, gps_msg.latdeg) # north-south, latitude
        new_y = math.copysign(gps_msg.longmin, gps_msg.longdeg) # east-west, longitude

        # update distance measurement, correct for bias
        self.gps_x = new_x - gps_x_mean
        self.gps_y = new_y - gps_y_mean

    def heading_update(self, heading_msg):
        self.heading = heading_msg.heading
        x_b = np.array([[cos(self.heading*pi), sin(self.heading*pi)]])
        y_b = np.array([[-sin(self.heading*pi), cos(self.heading*pi)]])
        self.kf_x.B = np.dot(self.discrete_b, x_b)
        self.kf_y.B = np.dot(self.discrete_b, y_b)

        

def main(args=None):
    rclpy.init(args=args)

    kalman = KalmanNode()

    rclpy.spin(kalman)

    #rpm_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()


