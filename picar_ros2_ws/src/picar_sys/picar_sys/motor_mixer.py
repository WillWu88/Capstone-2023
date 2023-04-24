import rclpy
from rclpy.node import Node
import drivers.motor_driver

class MotorMixer(Node):

    def __init__(self):
        super().__init__('motor mixer')
        self.driver = drivers.motor_driver.MotorDriver()
        self.command_sub = self.create_subscription()
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg_count = 0



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

