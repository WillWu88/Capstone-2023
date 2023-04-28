import numpy as np
import rclpy
from math import atan, copysign, pi, degrees
from rclpy.node import Node
import drivers.navigation_driver
from tutorial_interfaces import VelSetpoint, Heading, PoseSetpoint, XFiltered
from drivers.car_param import *
from drivers.navigation_points import *
from drivers.gps_helper import *

class Navigation(Node):

    def __init__(self):
        super().__init__('navigation_publisher')
        # Publishers
        self.heading_pub = self.create_publisher(Heading, 'heading', 10)
        self.pose_pub = self.create_publisher(PoseSetpoint, 'pose_setpoint', 10)
        self.vel_pub = self.create_publisher(VelSetpoint, 'vel_setpoint', 10)
        
        # Subscribers
        self.kf_sub = self.create_subscription(XFiltered, 'x_filtered', self.kf_callback, 10)
        self.origin_x = ORIGIN_X
        self.origin_y = ORIGIN_Y
        self.curr_x = ORIGIN_X
        self.curr_y = ORIGIN_Y
        self.heading = 0.
        self.turn_now = False
        self.turn_angle = -4;

        # heading is in radians, but servo control is in degrees

        # Timer period
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Set point
        msg_setpoint  = self.populate_message(self, 'pose_set_point')
        self.publisher_.publish(msg_setpoint)

        # Vel set point
        msg_velsetpoint = self.populate_message(self, 'vel_set_point')
        self.publisher_.publish(msg_velsetpoint)

        # Heading
        msg_heading = self.populate_message(self,'heading')
        self.publisher_.publish(msg_heading)

    
    def kf_callback(self,msg):
        self.curr_x = msg.xpos
        self.curr_y = msg.ypos
        if self.car_arrived():
            point_q.pop[0]
            match is_turn_q.pop[0]:
                case is_turn_status["heading_change"]:
                    self.heading -= 0.5
                    self.turn_now = False
                case is_turn_status["turn"]:
                    self.turn_now = True
                case _:
                    self.turn_now = False

    def populate_message(self, msg_type):
        match msg_type:
            case 'pose_set_point':
                msg = PoseSetpoint()
                msg.xsetpoint = self.xsetpoint_callback()
                msg.ysetpoint = self.ysetpoint_callback()
                msg.yawsetpoint = self.yawsetpoint_callback()
                msg.header.frame_id = 'earth'
            case 'vel_set_point':
                msg = VelSetpoint()
                msg.target = self.velsetpoint_callback()
                msg.header.frame_id = 'body'
            case 'heading':
                msg = Heading()
                msg.heading = self.heading_callback()
                msg.header.frame_id = 'earth'
        # Header
        msg.header.stamp = self.get_clock().now().to_msg()
        return msg
    
    def xsetpoint_callback(self): 
        return point_q[0][coord_label["lat"]] # peek the queue

    def ysetpoint_callback(self):
        return point_q[0][coord_label["long"]] # peek the queue

    def velsetpoint_callback(self):
        target_vel = 2.5 #m/s
        return target_vel

    def yawsetpoint_callback(self):
        if not(self.turn_now):
            try:
                if self.heading % 1 != 0:
                    self.frac = ((self.curr_x - ORIGIN_X)/(self.curr_y - ORIGIN_Y))
                else:
                    self.frac = -1/((self.curr_x - ORIGIN_X)/(self.curr_y - ORIGIN_Y))
            except ZeroDivisionError:
                if self.heading % 1 != 0:
                    self.frac = copysign(pi/2, self.curr_x - ORIGIN_X)
                else:
                    self.frac = copysign(pi/2, self.curr_y - ORIGIN_Y)
            return atan(self.frac)
        else:
            return self.turn_angle 

    def heading_callback(self):
        return self.heading


    def car_arrived(self):
        x_dist = approx_distance_lat(self.origin_x, self.curr_x) ** 2
        y_dist = approx_distance_lat(self.origin_y, self.curr_y) ** 2
                   
        if (x_dist + y_dist) < 0.2:
            return True
        else:
            return False

def main(args=None):
    rclpy.init(args=args)

    navigation_publisher = Navigation()

    rclpy.spin(navigation_publisher)

    rclpy.shutdown()

if __name__ == '__main__':
    main()


