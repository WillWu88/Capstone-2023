import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Header
import drivers.gps_driver
from tutorial_interfaces.msg import GPS

class GpsPublisher(Node):

    def __init__(self):
        super().__init__('gps_publisher')
        self.size = 5
        self.gps = drivers.gps_driver.GPSDriver()
        self.publisher = self.create_publisher(GPS, 'gps_raw', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0
        self.flag = True

    def timer_callback(self):
        self.gps.update()
        msg = self.populate_message()
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%f"' % msg.longitude_degrees)
        self.msg_count +=1

    def populate_message(self):
        msg = GPS()
        #Header
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = ''
        msg.longdeg = self.gps.data[self.gps.index_dict['long_deg']]
        msg.longmin = self.gps.data[self.gps.index_dict['long_min']]
        msg.latdeg = self.gps.data[self.gps.index_dict['lat_deg']]
        msg.latmin = self.gps.data[self.gps.index_dict['lat_min']]
        msg.flag = self.flag
        self.flag = not(self.flag)
        return msg
        

def main(args=None):
    rclpy.init(args=args)

    gps_publisher = GpsPublisher()

    rclpy.spin(gps_publisher)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
