import numpy as np
import rclpy
from math import atan, copysign, pi, degrees, sqrt
from rclpy.node import Node
import drivers.navigation_driver
from tutorial_interfaces.msg import VelSetpoint, Heading, PoseSetpoint, XFiltered, GPS
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
        self.gps_sub = self.create_subscription(GPS, 'gps_raw', self.gps_callback, 10)

        # gps origin and drift correction
        self.lat_correction = 0
        self.long_correction = 0
        self.curr_lat_origin = origin_lat_min
        self.curr_long_origin = origin_long_min
        self.drift_corrected = False
        self.drift_spacing = 4
        self.curr_x = 0
        self.target_x = 0
        
        self.heading = 0.
        self.turn_now = False
        self.turn_angle = 4;

        # heading is in radians, but servo control is in degrees

        # Timer period
        timer_period = 0.2 # seconds, currently at 5hz update
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # velocity control
        self.target_vel = 1.3 #m/s
        self.stop_now = False

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

    
    def kf_callback(self, msg):
        self.curr_x = msg.weighted_x_pos
        # only continue if car has arrived at the current
        # but not last waypoint
        if (self.car_arrived() and not self.stop_now):
            last_point = point_q.pop(0)
            if not(len(point_q)):
                self.get_logger().info("Stopping")
                self.stop_now = True
                return
            ret  = is_turn_q.pop(0);
            heading_change = is_turn_status["heading_change"]
            turn = is_turn_status["turn"]
            if (ret == heading_change):
                self.curr_long_origin = last_point[coord_label["long"]] - self.long_correction
                self.curr_lat_origin = last_point[coord_label["lat"]] - self.lat_correction
                self.update_target()
                self.heading -= 0.5
                self.turn_now = False
            elif (ret == turn):
                # execute turn, 4 meters
                self.target_x += 7
                self.turn_now = True
            else:
                self.turn_now = False


    def gps_callback(self,msg):
        if (not(self.drift_corrected)):
            new_lat_org = msg.latmin
            new_long_org = -msg.longmin
            self.lat_correction = origin_lat_min - new_lat_org
            self.long_correction = origin_long_min - new_long_org
            
            # calculate new target distance
            self.update_target()
            if (self.drift_spacing == 0):
                self.drift_corrected = True
            else:
                self.drift_spacing -= 1

    def populate_message(self, msg_type):
        match msg_type:
            case 'pose_set_point':
                msg = PoseSetpoint()
                # peek the queue
                msg.yawsetpoint = -0.015 # stay straight
                msg.macro_heading = self.heading
                msg.header.frame_id = 'earth'
                msg.turning_override = self.turn_now
            case 'vel_set_point':
                msg = VelSetpoint()
                msg.target = self.target_vel
                msg.kill_switch = self.stop_now
                msg.header.frame_id = 'body'
            case 'heading':
                msg = Heading()
                msg.heading = self.heading
                msg.header.frame_id = 'earth'
        # Header
        msg.header.stamp = self.get_clock().now().to_msg()
        return msg
    
    def car_arrived(self):
        if (self.curr_x - self.target_x) ** 2 < 0.2:
            return True
        else:
            return False

    def update_target(self):
        # calculate the distance needed between current target and current origin
        y_dist = approx_distance_lon(self.curr_long_origin, 
                        point_q[0][coord_label["long"]] - self.long_correction)
        x_dist = approx_distance_lat(self.curr_lat_origin, 
                        point_q[0][coord_label["lat"]] - self.lat_correction)
        self.target_x = sqrt(x_dist ** 2 + y_dist ** 2) * gps_sens_factor
        self.get_logger().info("Target distance updated, %f" % self.target_x)

def main(args=None):
    rclpy.init(args=args)

    navigation_publisher = Navigation()

    rclpy.spin(navigation_publisher)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
