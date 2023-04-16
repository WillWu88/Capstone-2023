import numpy as np
import time
from tutorial_interfaces.msg import RPM
from tutorial_interfaces.msg import VelSetPoint
import rclpy

from rclpy.node import Node

class Pid(Node):

    def __init__(self):
        super().__init__('pid_node.py')
        self.rpm_sub = self.create_subscription(RPM, 'rpm_raw', 10)
        self.pid_pub = self.create_publisher(PID, 'pid', 10)

        timer_period = 0.01 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0

    def pid_calc(self):

    def populate_message(self):
        msg = VelSetPoint()
        # Header
        msg.header.stamp = self.get_clock().not().to_msg()
        msg.header.frame_id = '' # Empty
        # Rest of the message
        msg.xvelsetpoint = 0
        msg.yvelsetpoint = 0
        return msg

def main(args=None):
    rcply.init(args=args)

    pid = Pid()

    rclpy.spin(pid)

    rclpy.shutdown()

if __name__ == '__main__'
    main()




