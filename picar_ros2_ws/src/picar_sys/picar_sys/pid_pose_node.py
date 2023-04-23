import numpy as np
import time
from tutorial_interfaces.msg import Heading, PoseSetPoint, PIDPOSE
import rclpy
import drivers.pid_driver
from drivers.pid_constant import *

from rclpy.node import Node

class PidPose(Node):

    def __init__(self):
        # Super constructor
        super().__init__('pid_pose_node')

        # Subscriber
        self.kfyaw_sub = self.create_subscription(Heading, 'heading', 
                                                self.heading_callback, 10)
        self.posesetpoint_sub = self.create_subscription(PoseSet, 'pose_set', 
                                                self.poseset_callback, 10)
        # Publisher
        self.pid_pose_pub = self.create_publisher(PIDPOSE, 'theta', 10)

        # Time period
        timer_period = 0.05 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0

        self.pid_driver = drivers.pid_driver.PidDriver(Kp_pose, Ki_pose, Kd_pose, 1/timer_period)

    def heading_callback(self, msg):
        self.pid_driver.curr_state = msg.heading
        self.get_logger().info('Received heading info: "%f"' %msg.heading)
 
    def poseset_callback(self, msg):
        self.pid_driver.setpoint = msg.yawsetpoint
        self.get_logger().info('Received Yaw setpoint: "%f"' %msg.yawsetpoint)
    
    def timer_callback(self):
        msg = populate_message()
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%f"' %msg.theta)
        self.msg_count +=1
        self.pid_driver.update()
 
    def populate_message(self):
        msg = PIDPOSE()
        # Header
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'body'
        # Rest of the message
        msg.theta = pid_driver.pid_calc()
        return msg


def main(args=None):
    rclpy.init(args=args)

    pid_pose = PidPose()

    rclpy.spin(pid_pose)

    rclpy.shutdown()

if __name__ == '__main__':
    main()


