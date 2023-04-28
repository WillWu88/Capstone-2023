import rclpy
from rclpy.node import Node
import drivers.steer_driver
from tutorial_interfaces.msg import PIDPOSE

class ServoNode(Node):

    def __init__(self):
        # Super constructor
        super().__init__('servo node')

        # Driver
        self.driver = drivers.steer_driver.SteerDriver()
        
        # Subscriber
        self.angle_sub = self.create_subscripion(PIDPOSE, 'theta', 10)
        
        timer_period = 0.01 #seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0

    def timer_callback(self):
        pass       
