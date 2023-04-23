import numpy as np
import time
from tutorial_interfaces.msg import VelSetpoint, XFiltered, PIDVEL
import rclpy
import drivers.pid_driver
from drivers.pid_constant import *

from rclpy.node import Node

class PidVel(Node):

    def __init__(self):
        # Super constructor
        super().__init__('pid_node')
        
        # Pid Driver

        # Subscriber
        self.kfx_sub = self.create_subscription(XFiltered, 'x_filtered', 
                                                self.xfiltered_callback, 10)
        self.vel_set = self.create_subscription(VelSet, 'vel_set', 
                                                self.velset_callback, 10)
        # Publisher
        self.pid_pub = self.create_publisher(PIDVEL, 'tau', 10)

        # Time period
        timer_period = 0.05 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0

        self.pid_driver = drivers.pid_driver.PidDriver(Kp_vel, Ki_vel, Kd_vel, 1/timer_period)

    def xfiltered_callback(self, msg):
        self.pid_driver.curr_state = msg.xbvel
        self.get_logger().info('Received xvel info: "%f"' %msg.xbvel)
 
    def velset_callback(self, msg):
        self.pid_driver.setpoint = msg.target
        self.get_logger().info('Received velsetpoint: "%f"' %msg.target)
    
    def timer_callback(self):
        msg = populate_message()
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%f"' %msg.tau)
        self.msg_count +=1
        self.pid_driver.update()
 
    def populate_message(self):
        msg = PIDVEL()
        # Header
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'body'
        # Rest of the message
        msg.tau = pid_driver.pid_calc()
        return msg


def main(args=None):
    rclpy.init(args=args)

    pid_vel = PidVel()

    rclpy.spin(pid_vel)

    rclpy.shutdown()

if __name__ == '__main__':
    main()


