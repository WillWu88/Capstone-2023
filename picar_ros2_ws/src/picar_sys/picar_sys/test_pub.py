import rclpy
from rclpy.node import Node
from math import atan
from tutorial_interfaces.msg import VelSetpoint, PIDVEL, PIDPOSE, PoseSetpoint, XFiltered
from drivers.navigation_points import *
from drivers.car_param import *

class TestPub(Node):

    def __init__(self):
        super().__init__('test_pub')
        #self.test_pub = self.create_publisher(PIDVEL, 'tau', 10)
        #self.test_pub2 = self.create_publisher(VelSetpoint, 'vel_setpoint', 10)
        self.test_pub3 = self.create_publisher(PIDPOSE, 'theta', 10)
        self.test_pub4 = self.create_publisher(PoseSetpoint, 'pose_setpoint', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.x_sub = self.create_subscription(XFiltered, 'x_filtered', self.x_sub_callback, 10)
        self.curr_x = ORIGIN_X
        self.curr_y = ORIGIN_Y

    def timer_callback(self):
        # msg = PIDVEL()
        # msg.tau = 0.15
        # msg.header.frame_id = 'body'
        # msg.header.stamp = self.get_clock().now().to_msg()
        # self.test_pub.publish(msg)
        # msg2 = VelSetpoint()
        # msg2.target = 2.5
        # msg2.header.frame_id = 'body'
        # msg2.header.stamp = self.get_clock().now().to_msg()
        # self.test_pub2.publish(msg2)
        # msg3 = PIDPOSE()
        # msg3.theta = 28.
        # msg3.header.frame_id = 'body'
        # msg3.header.stamp = self.get_clock().now().to_msg()
        # self.test_pub3.publish(msg3)
        # self.get_logger().info('Publishing setpoint')
        msg4 = PoseSetpoint()
        msg4.header.frame_id = 'body'
        msg4.xsetpoint = p1_lat_min
        msg4.ysetpoint = p1_long_min
        msg4.yawsetpoint = atan((self.curr_y - ORIGIN_Y) / (ORIGIN_X - self.curr_x))
        msg4.header.stamp = self.get_clock().now().to_msg()
        self.test_pub4.publish(msg4)
        self.get_logger().info('Publishing setpoint')

    def x_sub_callback(self, msg):
        self.curr_x = msg.xpos
        self.curr_y = msg.ypos



def main(args=None):
    rclpy.init(args=args)

    test_publisher = TestPub()

    rclpy.spin(test_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    # test_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

