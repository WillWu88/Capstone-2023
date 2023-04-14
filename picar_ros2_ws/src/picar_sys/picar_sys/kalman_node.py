import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Header
from sensor_msgs.msg import Imu
from tutorial_interfaces.msg import GPS, PoseSetpoint, RPM, VelSetpoint, XFiltered, YawFiltered, YFiltered
from message_filters import Subscriber
from filterpy.kalman import KalmanFilter

class KalmanX(Node):


    def __init__(self):
        super().__init__('kalman_filter_x')
        self.x_pub = self.create_publisher(XFiltered, 'x_filtered', 10) # history depth of 10
        self.y_pub = self.create_publisher(YFiltered, 'y_filtered', 10)
        self.psi_pub = self.create_publisher(YawFiltered, 'yaw_filtered', 10)

        self.:

    def timer_callback(self):
        


def main(args=None):
    rclpy.init(args=args)

    kalman_x = KalmanX()

    rclpy.spin(kalman_x)

    #rpm_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()


