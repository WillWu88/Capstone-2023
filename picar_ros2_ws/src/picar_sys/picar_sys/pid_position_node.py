import rclpy
import drivers.pid_driver
from drivers.pid_constant import *
from rclpy.node import Node
from math import atan
from tutorial_interfaces.msg import VelSetpoint, XFiltered

class PositionControl(Node):

    def __init__(self):
        super().__init__('position_ctrl')
        self.position_pub = self.create_publisher(VelSetpoint, 'vel_setpoint', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.x_sub = self.create_subscription(XFiltered, 'x_filtered_fast', self.x_sub_callback, 10)
        self.pid = drivers.pid_driver.PidDriver(Kp_pos, Ki_pos, Kd_pos, 1/timer_period, 2.3)
        self.pid.setpoint = 3

    def timer_callback(self):
        msg = VelSetpoint()
        msg.header.frame_id = 'body'
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.target = float(self.pid.pid_calc())
        self.pid.update()
        self.position_pub.publish(msg)


    def x_sub_callback(self, msg):
        self.pid.curr_state = msg.xpos
        self.pid.error_calc()

def main(args=None):
    rclpy.init(args=args)

    position_ctrl = PositionControl()

    rclpy.spin(position_ctrl)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    # test_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

