import numpy as np
import time
from tutorial_interfaces.msg import Heading, PoseSetpoint, PIDPOSE, XFiltered
import rclpy
import drivers.pid_driver
from drivers.pid_constant import *
from drivers.car_param import *
from drivers.navigation_points import *
from math import atan, pi, copysign

from rclpy.node import Node

class PidPose(Node):

    def __init__(self):
        # Super constructor
        super().__init__('pid_pose_node')

        # Subscriber
        self.curr_heading = 0.
        self.kfx_sub = self.create_subscription(XFiltered, 'x_filtered_fast', 
                                                self.xfiltered_callback, 10)
        self.posesetpoint_sub = self.create_subscription(PoseSetpoint, 'pose_setpoint',
                                                self.poseset_callback, 10)
        # Publisher
        self.pid_pose_pub = self.create_publisher(PIDPOSE, 'theta', 10)

        # Time period
        timer_period = 0.025 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.pid_driver = drivers.pid_driver.PidDriver(Kp_pose, Ki_pose, Kd_pose, 
                                                        1/timer_period, 1.5, -1.5)
        self.heading = 0.
        self.x_set = point_q[0][0]
        self.y_set = point_q[0][1]
        self.turn_now = False


    def xfiltered_callback(self, msg):
        # yaw rate control
        self.pid_driver.curr_state = msg.yawvel
        self.pid_driver.error_calc()
        # self.pid_driver.e1 += 0.5
 
    def poseset_callback(self, msg):
        self.pid_driver.setpoint = msg.yawsetpoint
        self.turn_now = msg.turning_override
        # self.get_logger().info('Received Yaw setpoint: "%f"' %msg.yawsetpoint)
    
    def timer_callback(self):
        msg = self.populate_message()
        self.pid_pose_pub.publish(msg)
        # self.get_logger().info('Publishing: "%f"' %msg.theta)
        self.pid_driver.update()
 
    def populate_message(self):
        msg = PIDPOSE()
        # Header
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'body'
        # Rest of the message
        if (self.turn_now):
            msg.theta = 5.5
        else:
            msg.theta = float(self.pid_driver.pid_calc())
        msg.debug_error = self.pid_driver.e1
        return msg


def main(args=None):
    rclpy.init(args=args)

    pid_pose = PidPose()

    rclpy.spin(pid_pose)

    rclpy.shutdown()

if __name__ == '__main__':
    main()


