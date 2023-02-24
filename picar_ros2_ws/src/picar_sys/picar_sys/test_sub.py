import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu


class TestSubscriber(Node):

    def __init__(self):
        super().__init__('test_subscriber')
        self.subscription = self.create_subscription(Imu,
                                                    'imu_raw',
                                                    self.imu_callback,
                                                    10)
        self.subscription  # prevent unused variable warning

    def imu_callback(self, msg):
        self.get_logger().info('Time stamp: ' + str(msg.header.stamp))
        # test reception on x-axis
        self.get_logger().info('x feedback: "%f"' %msg.linear_acceleration.x)


def main(args=None):
    rclpy.init(args=args)

    test_sub = TestSubscriber()
    rclpy.spin(test_sub)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
