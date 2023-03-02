import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Header
from geometry_msgs.msg import Vector3, Quaternion
from sensor_msgs.msg import Temperature

class EncoderPublisher(Node):
    def __init__(self):
        self.encoder = drivers.encoder_driver.EncoderDriver()
        self.publisher_ = self.create_publisher(Encoder, 'encoder_raw', 10)
        timer_period = 0.001
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0

    def timer_callback(self):

        #self.imu.update()
        msg = self.populate_message()

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % self.msg_count)
        self.msg_count += 1

    def populate_message(self) -> Temperature:
        # put current encoder data into msg

        msg = Temperature() # type of sensor message we want

        # header config
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = '' #empty for now

        # sensor data here
        msg.variance = self.encoder.data[self.imu.index_dict['raw_rpm']]
        msg.temperature = self.encoder.data[self.imu.index_dict['filtered_rpm']]

        return msg

    
def main(args=None):
    rclpy.init(args=args)

    rpm_publisher = EncoderPublisher()

    rclpy.spin(rpm_publisher)

    rpm_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
