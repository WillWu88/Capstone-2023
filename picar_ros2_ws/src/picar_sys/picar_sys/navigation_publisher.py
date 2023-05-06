import numpy as np
import rclpy
from math import atan, copysign, pi, degrees
from rclpy.node import Node
import drivers.navigation_driver
from tutorial_interfaces.msg import VelSetpoint, Heading, PoseSetpoint, XFiltered, GPS
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
        # self.kf_sub = self.create_subscription(XFiltered, 'x_filtered', self.kf_callback, 10)
        self.gps_sub = self.create_subscription(GPS, 'gps_raw', self.kf_callback, 10)
        self.origin_x = ORIGIN_X
        self.origin_y = ORIGIN_Y
        self.curr_x = ORIGIN_X
        self.curr_y = ORIGIN_Y
        self.heading = 0.
        self.turn_now = False
        self.turn_angle = 4;

        # heading is in radians, but servo control is in degrees

        # Timer period
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Set point
        msg_setpoint  = self.populate_message('pose_set_point')
        self.pose_pub.publish(msg_setpoint)

        # Vel set point
        msg_velsetpoint = self.populate_message('vel_set_point')
        self.vel_pub.publish(msg_velsetpoint)

        # Heading
        msg_heading = self.populate_message('heading')
        self.heading_pub.publish(msg_heading)

    
    def kf_callback(self,msg):
        # self.curr_x = msg.xpos*0.002160 + 64.8417 # hard code fix later. Reverse approx distance
        # self.curr_y = -30.2358 + 0.00274*msg.ypos
        self.curr_x = msg.latmin
        self.curr_y = -msg.longmin
        if self.car_arrived():
            if not(len(point_q)):
                # we have reached our last point
                raise SystemExit
                return
            point_q.pop(0)
            ret  = is_turn_q.pop(0);
            heading_change = is_turn_status["heading_change"]
            turn = is_turn_status["turn"]
            if (ret == heading_change):
                self.heading -= 0.5
                self.turn_now = False
            elif (ret == turn):
                self.turn_now = True
            else:
                self.turn_now = False

    def populate_message(self, msg_type):
        match msg_type:
            case 'pose_set_point':
                msg = PoseSetpoint()
                msg.xsetpoint = self.xsetpoint_callback()
                msg.ysetpoint = self.ysetpoint_callback()
                msg.yawsetpoint = self.yawsetpoint_callback()
                msg.heading = self.heading
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
                    self.frac = (self.curr_x - point_q[0][coord_label["lat"]])/(self.curr_y - point_q[0][coord_label["long"]])
                else:
                    self.frac = -1/((self.curr_x - point_q[0][coord_label["lat"]])
                                /(self.curr_y - point_q[0][coord_label["long"]]))
            except ZeroDivisionError:
                if self.heading % 1 != 0:
                    self.frac = 0
                else:
                    self.frac = 0
            return atan(self.frac)
        else:
            return self.turn_angle 

    def heading_callback(self):
        return self.heading


    def car_arrived(self):
        x_dist = approx_distance_lat(point_q[0][coord_label["lat"]], self.curr_x) ** 2
        y_dist = approx_distance_lon(point_q[0][coord_label["long"]], self.curr_y) ** 2
                   
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
