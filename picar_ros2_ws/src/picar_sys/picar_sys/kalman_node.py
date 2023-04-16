import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Header
from sensor_msgs.msg import Imu
from tutorial_interfaces.msg import GPS, PoseSetpoint, RPM, VelSetpoint, XFiltered, YawFiltered, YFiltered
from message_filters import TimeSynchronizer, Subscriber
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise

class KalmanX(Node):


    def __init__(self):
        super().__init__('kalman_filter_x')
        self.x_pub = self.create_publisher(XFiltered, 'x_filtered', 10) 
        self.y_pub = self.create_publisher(YFiltered, 'y_filtered', 10)
        self.psi_pub = self.create_publisher(YawFiltered, 'yaw_filtered', 10)

        self.imu_sub = Subscriber(self, Imu, 'imu_raw') #qos profile always 10
        self.rpm_sub = Subscriber(self, RPM, 'rpm_raw') 
        self.time_sync = TimeSynchronizer([self.imu_sub, self.rpm_sub], 10)
        self.time_sync.registerCallback(kf_update)

        self.f_s = 100.0
        self.kf_x = KalmanFilter(dim_x=2, dim_z=1)
        self.kf_init(self.kf_x, self.f_s, np.array([0, 1]), rpm_cov, 
                     Q_discrete_white_noise(2, 1./self.f_s, var=imu_x_var))

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
        pass



def main(args=None):
    rclpy.init(args=args)

    kalman_x = KalmanX()

    rclpy.spin(kalman_x)

    #rpm_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()


