import rclpy
from rclpy.node import Node
import drivers.steer_driver
from tutorial_interfaces.msg import PIDPOSE

class ServoNode(Node):

    def __init__(self):
        # Super constructor
        super().__init__('servo_node')

        # Driver
        self.steer_driver = drivers.steer_driver.ServoDriver()
        
        # Subscriber
        self.angle_sub = self.create_subscription(PIDPOSE, 'theta', self.theta_callback, 10)
        self.theta = 0.
        self.curr = 0.

    def theta_callback(self,msg):
        self.theta = msg.theta
        if (self.curr != self.theta):
            self.steer_driver.setAngle(self.theta)

def main(args=None):
    rclpy.init(args=args)

    servo_node = ServoNode()

    rclpy.spin(servo_node)

    #rpm_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
