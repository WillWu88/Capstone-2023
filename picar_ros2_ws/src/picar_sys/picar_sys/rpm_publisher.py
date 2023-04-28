import rclpy
import time
from rclpy.node import Node
import drivers.rpm_serial_driver
from tutorial_interfaces.msg import RPM
from drivers.kf_constants import *
from drivers.car_param import *

class RpmPublisher(Node):


    def __init__(self):
        super().__init__('rpm_publisher')
        self.size = 5
        self.encoder = drivers.rpm_serial_driver.EncoderDriver()
        self.publisher = self.create_publisher(RPM, 'rpm_raw', 10) # history depth of 10
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0

    def timer_callback(self):
        
        self.encoder.update()
        msg = self.populate_message()

        self.publisher.publish(msg)
        if (not(self.msg_count)):
            self.get_logger().info('Publishing: "%f"' % msg.rpmfiltered)
            self.msg_count += 1

    def populate_message(self):
        msg = RPM()
        # Header 
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = '' #empty for now
        msg.rpmraw = 0.0
        filtered_rpm = self.encoder.update()
        msg.rpmfiltered = filtered_rpm
        msg.derivedms = 3.1415*filtered_rpm*wheel_diam/60.0

        return msg

def main(args=None):
    rclpy.init(args=args)

    rpm_publisher = RpmPublisher()

    rclpy.spin(rpm_publisher)

    #rpm_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()


