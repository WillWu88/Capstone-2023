import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Header
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3, Quaternion
import drivers.imu_driver 

class IMUPublisher(Node):

    def __init__(self):
        super().__init__('imu_publisher')
        self.imu = drivers.imu_driver.IMUDriver()
        self.publisher_ = self.create_publisher(Imu, 'imu_raw', 10) # history depty of 10
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0

    def timer_callback(self):

        self.imu.update()
        msg = self.populate_message()

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % self.msg_count)
        self.msg_count += 1

    def populate_message(self) -> Imu:
        # put current imu data into msg

        msg = Imu()

        # header config
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = '' #empty for now

        # keeping at 0 for now, estimator relevant
        msg.orientation = Quaternion()
        msg.orientation_covariance = [0.0] * 9
        msg.angular_velocity_covariance = [0.0] * 9
        msg.linear_acceleration_covariance = [0.0] * 9

        # sensor data here
        msg.angular_velocity.x = self.imu.data[self.imu.index_dict['gyro_x']] 
        msg.angular_velocity.y = self.imu.data[self.imu.index_dict['gyro_y']] 
        msg.angular_velocity.z = self.imu.data[self.imu.index_dict['gyro_z']] 

        msg.linear_acceleration.x = self.imu.data[self.imu.index_dict['acc_x']] 
        msg.linear_acceleration.y = self.imu.data[self.imu.index_dict['acc_y']] 
        msg.linear_acceleration.z = self.imu.data[self.imu.index_dict['acc_z']] 

        return msg


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

