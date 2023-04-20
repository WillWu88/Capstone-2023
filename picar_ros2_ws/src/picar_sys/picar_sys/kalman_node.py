import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Header
from sensor_msgs.msg import Imu
from tutorial_interfaces.msg import GPS, PoseSetpoint, RPM, VelSetpoint, XFiltered, YawFiltered, YFiltered
from message_filters import TimeSynchronizer, Subscriber
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
import drivers.sensor_noise
import drivers.kf_constants

class KalmanNode(Node):

    def __init__(self):
        super().__init__('kalman_filter_x')
        self.x_pub = self.create_publisher(XFiltered, 'x_filtered', 10) 
        self.y_pub = self.create_publisher(YFiltered, 'y_filtered', 10)
        self.psi_pub = self.create_publisher(YawFiltered, 'yaw_filtered', 10)

        self.imu_sub = Subscriber(self, Imu, 'imu_raw') #qos profile always 10
        self.rpm_sub = Subscriber(self, RPM, 'rpm_raw') 
        # time synchronizer
        self.time_sync = TimeSynchronizer([self.imu_sub, self.rpm_sub], 10)
        self.time_sync.registerCallback(self.kf_update)

        self.f_s = 100.0
        self.kf_x = KalmanFilter(dim_x=2, dim_z=1)
        self.kf_init(self.kf_x, self.f_s, np.array([0, 1]), rpm_cov, 
                     Q_discrete_white_noise(2, 1./self.f_s, var=imu_x_var))

        self.kf_y = KalmanFilter(dim_x=2, dim_z=1)
        self.kf_init(self.kf_y, self.f_s, np.array([0, 1]), gps_cov,
                     Q_discrete_white_noise(2, 1./self.f_s, var=imu_y_var))

        self.kf_psi = KalmanFilter(dim_x=1, dim_z=1)
        self.kf_init(self.kf_psi, self.f_s, np.array([1]), tan_cov,
                     Q_discrete_white_noise(1, 1./self.f_s, var=imu_psi_var))

        # GPS fusion, expand after normal kf
        self.gps_sub = self.create_subscription(GPS, 'gps_raw', self.gps_callback, 10)

    def kf_init(self, kf, f_s, custom_H, custom_R, custom_Q):
        '''default: dt double integrator F=ma process 
            initial covariance set to identity
        '''
        kf.F = np.array([[1., 1/f_s],[0., 1.]])
        kf.B = np.array([[1./(f_s*f_s*2.)],[1./f_s]]) # imu input
        kf.H = custom_H
        kf.R = custom_R
        kf.Q = custom_Q

    def kf_update(self, imu_msg, rpm_msg):
        try:
            assert imu_msg.header.stamp == rpm.header.stamp
        except AssertionError:
            self.get_logger().info("Time stamp mismatch")
        else:
            u_x = np.array([[0],[imu_msg.linear_acceleration.x]])
            z_x = np.array([[0],[rpm_msg.rpmfiltered]])
            self.kf_x.predict(u=u_x)
            self.kf_x.update(z_x)

            x_msg = XFiltered()
            x_msg.header.stamp = self.get_clock().now().to_msg()
            x_msg.header.frame_id = 'body' 
            x_msg.xpos = self.kf_x.x[0]
            x_msg.xpos = self.kf_x.x[1]
            self.x_pub.publish(x_msg)

    def gps_callback(self):
        self.get_logger().info('GPS Update Received')



def main(args=None):
    rclpy.init(args=args)

    kalman = KalmanNode()

    rclpy.spin(kalman)

    #rpm_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()


