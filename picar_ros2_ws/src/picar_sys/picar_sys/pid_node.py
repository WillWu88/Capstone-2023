from tutorial_interfaces.msg import VelSetpoint, XFiltered, PIDVEL, RPM
import rclpy
import drivers.pid_driver
from drivers.pid_constant import *

from rclpy.node import Node

class PidVel(Node):

    def __init__(self):
        # Super constructor
        super().__init__('pid_node')

        # Subscriber
        self.kfx_sub = self.create_subscription(XFiltered, 'x_filtered_fast', 
                                                self.xfiltered_callback, 10)
        # self.test_speed_sub = self.create_subscription(RPM, 'rpm_raw', self.rpm_callback, 10)
        self.vel_set = self.create_subscription(VelSetpoint, 'vel_setpoint', 
                                                self.velset_callback, 10)
        # Publisher
        self.pid_pub = self.create_publisher(PIDVEL, 'tau', 10)

        # Time period
        timer_period = 0.05 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.max_ctrl = 0.30 # maximum of 30% pwm
        self.min_ctrl = 0.10
        self.pid_driver = drivers.pid_driver.PidDriver(Kp_vel, Ki_vel, Kd_vel, 1/timer_period, self.max_ctrl, self.min_ctrl)
        self.stop_now = False

    def xfiltered_callback(self, msg):
        self.pid_driver.curr_state = msg.xbvel
        self.pid_driver.error_calc()
 
    def velset_callback(self, msg):
        if (msg.kill_switch):
            self.stop_now = True
        self.pid_driver.setpoint = msg.target
    
    def timer_callback(self):
        msg = self.populate_message()
        self.pid_pub.publish(msg)
        self.pid_driver.update()

    def rpm_callback(self, msg):
        self.pid_driver.curr_state = msg.derivedms
        self.pid_driver.error_calc()
 
    def populate_message(self):
        msg = PIDVEL()
        # Header
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'body'
        msg.debug_error = self.pid_driver.e1
        # Rest of the message
        if (self.stop_now):
            msg.kill_switch = True
            msg.tau = 0. # engine braking
        else:
            msg.tau = float(self.pid_driver.pid_calc())
        return msg


def main(args=None):
    rclpy.init(args=args)

    pid_vel = PidVel()

    rclpy.spin(pid_vel)

    rclpy.shutdown()

if __name__ == '__main__':
    main()


