import numpy as np
import time
from tutorial_interfaces.msg import VelSetPoint, XFiltered, YFiltered, PIDVEL
from messager_filters import TimeSynchronizer, Subscriber
import rclpy
import drivers.pid_driver

from rclpy.node import Node

class PidVel(Node):

    def __init__(self):
        # Super constructor
        super().__init__('pid_node.py')
        
        # Subscriber
        self.kfx_sub = Subscriber(self, XFiltered, 'x_filtered', qos_profile=10)
        self.kfy_sub = Subscriber(self, YFiltered, 'y_filtered', qos_profile=10)
        self.vel_set = Subscriber(self, VelSet, 'vel_set', qos_profile = 10)
        
        # Publisher
        self.pid_pub = self.create_publisher(PID, 'pid', 10)
        self.pid_calc = drivers.pid_driver.PidDriver()

        # Time synchronizer for the estimators
        self.time_sync = ApproximateTimeSynchronizer([self.kf_x, self.kf_y], 10)
        self.time_sync.registerCallback(self.sensor_update)
    
        # Time period
        timer_period = 0.05 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0

    def pid_update(self):
        self.get_logger().info('PID updating')
        try:
            assert kfx_sub.header.stamp == kfy_sub.header.stamp
        except AssertionError:
            self.get_logger().info("Time stamp mismatch")
        finally:
            


    def timer_callback(self):
        self.pid_calc.update()
        msg = populate_message()
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%f"' %msg.tau)
        self.msg_count +=1

    def populate_message(self):
        msg = PIDVEL()
        # Header
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = '' # Empty
        # Rest of the message
        msg.tau = 0
        return msg

def main(args=None):
    rcply.init(args=args)

    pid_vel = PidVel()

    rclpy.spin(pid_vel)

    rclpy.shutdown()

if __name__ == '__main__':
    main()




