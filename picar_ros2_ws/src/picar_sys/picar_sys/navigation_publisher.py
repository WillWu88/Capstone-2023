import numpy as np
import rclpy
from rclpy.node import Node
import drivers.navigation_driver
from tutorial_interfaces import VelSetpoint, Heading, PoseSetpoint, XFiltered
from drivers.car_param import *

class Navigation(Node):

    def __init__(self):
        super().__init__('navigation_publisher')
        # Publishers
        self.heading_pub = self.create_publisher(Heading, 'heading', 10)
        self.pose_pub = self.create_publisher(PoseSetpoint, 'pose_setpoint', 10)
        self.vel_pub = self.create_publisher(VelSetpoint, 'vel_setpoint', 10)
        
        # Subscribers
        self.kf_sub = self.create_subscription(XFiltered, 'x_filtered', self.kf_callback, 10)
        self.curr_x = ORIGIN_X
        self.curr_y = ORIGIN_Y

        # Timer period
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0

    def timer_callback(self):
        #self.get_logger().info('Publishing: "%f"' %msg.header.stamp)
        

    def kf_callback(self,msg):
        self.curr_x = msg.xpos
        self.curr_y = msg.ypos

    def populate_message(self, msg_type):
        match msg_type:
            case "pose_set_point":
                msg = PoseSetpoint()
                msg.xsetpoint = 0.
                msg.ysetpoint = 0.
            case 'vel_set_point':
                msg = VelSetpoint()
                msg.target =
            case 'heading':
                msg = Heading()
                msg.heading = 
        # Header
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'body'
        return msg
    
    def 


def main(args=None):
    rclpy.init(args=args)

    navigation_publisher = Navigation()

    rclpy.spin(navigation_publisher)

    rclpy.shutdown()

if __name__ == '__main__':
    main()


