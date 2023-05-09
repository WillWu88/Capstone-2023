import rclpy
from rclpy.node import Node
import drivers.motor_driver
from tutorial_interfaces.msg import PIDVEL

class MotorMixer(Node):

    def __init__(self):
        super().__init__('motor_mixer')
        self.driver = drivers.motor_driver.MotorDriver()
        self.command_sub = self.create_subscription(PIDVEL, 'tau', self.tau_callback, 10)
        self.tau = 0.
        self.curr = 0.
        self.timer = self.create_timer(0.005, self.timer_callback)
        self.stop_now = False

    def tau_callback(self, msg):
        self.tau = msg.tau
        self.stop_now = msg.kill_switch

    def timer_callback(self):
        if (self.stop_now):
            self.driver.Motor_Speed(0)
        if (self.curr != self.tau):
            self.driver.Motor_Speed(self.tau)
            self.curr = self.tau


def main(args=None):
    rclpy.init(args=args)

    motor_mixer = MotorMixer()

    rclpy.spin(motor_mixer)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    acc_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

