import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from snesor_msgs.msg import Imu
import imu_driver

class IMUPublisher(Node):

    def __init__(self):
        super().__init__('imu_publisher')
        self.imu = imu_driver.IMUDriver()
        self.publisher_ = self.create_publisher(Imu, 'imu_raw', 10) #history depty of 10
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    acc_publisher = IMUPublisher()

    rclpy.spin(acc_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    acc_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

