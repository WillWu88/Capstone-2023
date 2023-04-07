import rclpy
import time
from rclpy.node import Node
import drivers.encoder_driver
from tutorial_interfaces.msg import RPM

class RpmPublisher(Node):


    def __init__(self):
        super().__init__('rpm_publisher')
        self.size = 5
        self.encoder = drivers.encoder_driver.EncoderDriver(self.size)
        self.publisher_ = self.create_publisher(RPM, 'rpm', 10) # history depth of 10
        timer_period = 0.005  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0

    def timer_callback(self):
        
        self.encoder.update()
        msg = self.populate_message()

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % self.msg_count)
        self.msg_count += 1

    def populate_message(self) -> RPM:
        msg = RPM()
        # Header 
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = '' #empty for now
        msg.rpmraw = self.encoder.latest
        msg.rpmfiltered = self.encoder.CalcFilter()

        return msg

def main(args=None):
    rclpy.init(args=args)

    rpm_publisher = RpmPublisher()

    rclpy.spin(rpm_publisher)

    #rpm_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()


