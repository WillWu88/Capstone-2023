import numpy as np
import rclpy
import math
from rclpy.node import Node
from std_msgs.msg import String, Header
from sensor_msgs.msg import Imu
from tutorial_interfaces.msg import GPS, PoseSetpoint, RPM, VelSetpoint, XFiltered, YawFiltered, Origin
from message_filters import ApproximateTimeSynchronizer, Subscriber
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
from drivers.kf_constants import *
from drivers.car_param import *
import drivers.gps_helper

class KalmanNode(Node):

    def __init__(self):
        super().__init__('kalman_filter_x')
        self.x_pub = self.create_publisher(XFiltered, 'x_filtered', 10) 
        self.psi_pub = self.create_publisher(YawFiltered, 'yaw_filtered', 10)

        # x-axis kf config
        self.f_s = 100.0
        self.kf_x = KalmanFilter(dim_x=2, dim_z=1)
        self.kf_x.x = np.array([[0.0],[0.0]])
        self.kf_init(self.kf_x, self.f_s, np.array([[1., 0.], [0., 1.]]), 
                     ms_var * R_mult_x, 
                     Q_mult_x * Q_discrete_white_noise(2, 1./self.f_s, var=imu_x_var))

        self.kf_x.inv = np.reciprocal # numpy doesn't like 1-d inverse

        # yaw kf
        self.kf_psi = KalmanFilter(dim_x=1, dim_z=1)
        self.kf_init(self.kf_psi, self.f_s, np.array([[1.]]), tan_var * R_mult_psi,
                     Q_mult_psi * imu_psi_var, custom_F = np.array([[1.]]),
                     custom_B=np.array([[1./self.f_s]]))
        self.kf_psi.inv = np.reciprocal # numpy doesn't like 1-d inverse
        self.kf_psi.x = np.array([[0.0]])
        self.u_psi = 0.

        self.imu_sub = Subscriber(self, Imu, "/imu_raw", qos_profile=10) #qos profile always 10
        self.rpm_sub = Subscriber(self, RPM, "/rpm_raw", qos_profile=10) 
        # time synchronizer
        self.time_sync = ApproximateTimeSynchronizer([self.imu_sub, self.rpm_sub], 
                                                     10, 
                                                     0.01)

        self.time_sync.registerCallback(self.kf_update)

        # GPS fusion, expand after normal kf
        self.gps_sub = self.create_subscription(GPS, 'gps_raw', self.gps_callback, 10)
        self.origin_sub = self.create_subscription(Origin, 'origin', self.origin_update, 10)
        self.update_not_used = True # potential race condition?
        self.gps_x = 0.
        self.gps_y = 0.
        self.curr_heading = 0.
        self.origin_x = 0.
        self.origin_y = 0.

    def kf_init(self, kf, f_s, custom_H, custom_R, 
                custom_Q, custom_F=None, custom_B=None):
        '''default: dt double integrator F=ma process 
            initial covariance set to identity
        '''
        if custom_F==None:
            kf.F = np.array([[1., 1./f_s],[0., 1.]])
        else:
            kf.F = custom_F
        if custom_B==None:
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
            # remembers psi imu measurement
            self.u_psi = imu_msg.angular_velocity.z - imu_psi_mean

            self.kf_x.predict(u=u_x)
            vel_meas = rpm_msg.derivedms - ms_mean

            # gps fusion, update with GPS if coordinate is available
            if (self.update_not_used):
                self.get_logger().info('Updating with GPS')
                x_meas = gps_helper.approx_distance(self.origin_x, self.gps_x)
                y_meas = gps_helper.approx_distance(self.origin_y, self.gps_y)
                pos_meas = gps_helper.frame_transfer_x(self.curr_heading, x_meas, y_meas)
                self.update_not_used = False
            else: 
                # use previous state estimate if not available
                pos_meas = float(self.kf_x.x[0])
            

            v_x_meas = np.array([[pos_meas],[vel_meas]])
            self.kf_x.update(np.array([[v_x_meas]]))
            x_msg = XFiltered()
            x_msg.header.stamp = self.get_clock().now().to_msg()
            x_msg.header.frame_id = 'body' 
            x_msg.xpos = float(self.kf_x.x[0])
            x_msg.xvel = float(self.kf_x.x[1])
            self.x_pub.publish(x_msg)
            
            
            self.get_logger().info('Kalman X Updated')

    def gps_callback(self, gps_msg):
        self.update_not_used = True;
        # get new gps reading
        new_x = math.copysign(gps_msg.latmin, gps_msg.latdeg) # north-south, latitude
        new_y = math.copysign(gps_msg.longmin, gps_msg.longdeg) # east-west, longitude

        # GPS/IMU Heading fusion
        # GYRO measurement in deg/s
        self.kf_psi.predict(u=self.u_psi)
        
        try:
            heading_ratio = gps_helper.approx_distance(self.gps_y, new_y) / gps_helper.approx_distance(self.gps_x, new_x)
            psi_meas = math.degrees(math.atan(heading_ratio)) # result in degree
        except ZeroDivisionError:
            psi_meas = 0.0 # x axis will never be zero when the car is running
        pass

        self.kf_psi.update(psi_meas)
        # update psi estimate
        psi_msg = YawFiltered()
        psi_msg.header.stamp = self.get_clock().now().to_msg()
        psi_msg.header.frame_id = 'body'
        psi_msg.yawpos = float(self.kf_psi.x[0])
        psi_msg.yawmeas = float(psi_meas)
        self.psi_pub.publish(psi_msg)

        # update distance measurement
        self.gps_x = new_x
        self.gps_y = new_y

    def origin_update(self, new_origin):
        self.origin_x = math.copysign(new_origin.latmin, new_origin.latdeg) # north-south, latitude
        self.origin_y = math.copysign(new_origin.longmin, new_origin.longdeg) # east-west, longitude


        

def main(args=None):
    rclpy.init(args=args)

    kalman = KalmanNode()

    rclpy.spin(kalman)

    #rpm_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()


