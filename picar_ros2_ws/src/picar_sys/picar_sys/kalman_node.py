import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Header
from sensor_msgs.msg import Imu
from tutorial_interfaces.msg import GPS, PoseSetpoint, RPM, VelSetpoint, XFiltered, YawFiltered, YFiltered
from message_filters import ApproximateTimeSynchronizer, Subscriber
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
from drivers.kf_constants import *
from drivers.car_param import *

class KalmanNode(Node):

    def __init__(self):
        super().__init__('kalman_filter_x')
        self.x_pub = self.create_publisher(XFiltered, 'x_filtered', 10) 
        self.y_pub = self.create_publisher(YFiltered, 'y_filtered', 10)
        self.psi_pub = self.create_publisher(YawFiltered, 'yaw_filtered', 10)

        # x-axis kf config
        self.f_s = 100.0
        self.kf_x = KalmanFilter(dim_x=2, dim_z=1)
        self.kf_x.x = np.array([[0.0],[0.0]])
        self.kf_init(self.kf_x, self.f_s, np.array([[0., 1.]]), rpm_cov, 
                     Q_discrete_white_noise(2, 1./self.f_s, var=imu_x_var))
        self.kf_x.inv = np.reciprocal # numpy doesn't like 1-d inverse

        # y-axis kf
        self.kf_y = KalmanFilter(dim_x=2, dim_z=1)
        self.kf_init(self.kf_y, self.f_s, np.array([[0., 1.]]), gps_cov,
                     Q_discrete_white_noise(2., 1./self.f_s, var=imu_y_var))

        # yaw kf
        self.kf_psi = KalmanFilter(dim_x=1, dim_z=1)
        self.kf_init(self.kf_psi, self.f_s, np.array([[1.]]), tan_cov,
                     imu_psi_var)

        # GPS fusion, expand after normal kf
        self.gps_sub = self.create_subscription(GPS, 'gps_raw', self.gps_callback, 10)

        self.imu_sub = Subscriber(self, Imu, "/imu_raw", qos_profile=10) #qos profile always 10
        self.rpm_sub = Subscriber(self, RPM, "/rpm_raw", qos_profile=10) 
        # time synchronizer
        self.time_sync = ApproximateTimeSynchronizer([self.imu_sub, self.rpm_sub], 10, 0.01)
        self.time_sync.registerCallback(self.kf_update)

    def kf_init(self, kf, f_s, custom_H, custom_R, custom_Q):
        '''default: dt double integrator F=ma process 
            initial covariance set to identity
        '''
        kf.F = np.array([[1., 1./f_s],[0., 1.]])
        kf.B = np.array([[1./(f_s*f_s*2.)],[1./f_s]]) # imu input
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
            v_x_meas = 3.1415*wheel_diam*rpm_msg.rpmfiltered/60.0 #rpm to linear speed
            self.get_logger().info('Process: %f' % u_x)
            self.get_logger().info('Meas: %f' % v_x_meas)
            z_x = np.array([v_x_meas])
            self.kf_x.predict(u=u_x)
            try:
                self.kf_x.update(z_x)
            except np.linalg.LinAlgError:
                self.get_logger().info('S %f' % self.kf_x.S[0])
            except ValueError:
                self.get_logger().info('K 1: %f' % self.kf_x.K[0])
                self.get_logger().info('K 2: %f' % self.kf_x.K[1])

            x_msg = XFiltered()
            x_msg.header.stamp = self.get_clock().now().to_msg()
            x_msg.header.frame_id = 'body' 
            self.get_logger().info('X 1: %f' % self.kf_x.x[0])
            self.get_logger().info('X 2: %f' % self.kf_x.x[1])
            x_msg.xpos = float(self.kf_x.x[0])
            x_msg.xvel = float(self.kf_x.x[1])
            self.x_pub.publish(x_msg)
            self.get_logger().info('Kalman X Updated')

    def gps_callback(self, gps_msg):
        pass


def main(args=None):
    rclpy.init(args=args)

    kalman = KalmanNode()

    rclpy.spin(kalman)

    #rpm_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()


