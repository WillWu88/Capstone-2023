import numpy as np
import rclpy
from math import cos, sin, pi, degrees, atan
from rclpy.node import Node
from std_msgs.msg import String, Header
from sensor_msgs.msg import Imu
from tutorial_interfaces.msg import GPS, PoseSetpoint, RPM, VelSetpoint, XFiltered, Heading
from message_filters import ApproximateTimeSynchronizer, Subscriber
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
from drivers.kf_constants import *
from drivers.car_param import *
from drivers.gps_helper import *

class KalmanNode(Node):
    def __init__(self):
        super().__init__('kalman_filter_x')
        self.state_pub = self.create_publisher(XFiltered, 'x_filtered', 10) 
        self.fast_pub = self.create_publisher(XFiltered, 'x_filtered_fast', 10)

        self.heading_sub = self.create_subscription(Heading, 'heading', self.heading_update, 10)
        self.heading = 0.

        self.f_s = 100.0
        # body frame linear kalman filter for speed tracking, 100hz, non-gps fused
        self.kf_localx = KalmanFilter(dim_x=2, dim_z=1)
        self.kf_localx.x = np.array([[0.0], [0.0]])
        self.kf_init(self.kf_localx, self.f_s, np.array([[0., 1.]]), 
                     local_ms_mult * ms_var, 
                     Q_mult_local_x * Q_discrete_white_noise(2, 1./self.f_s, var=imu_x_var))

        # x-axis kf config, 10hz
        self.kf_x = KalmanFilter(dim_x=2, dim_z=1)
        self.kf_x.x = np.array([[0.0],[0.0]])
        self.discrete_b = np.array([[1./(self.f_s*self.f_s*2.)],
                                   [1./self.f_s]])

        # first row of rotation matrix
        x_b = np.array([[cos(self.heading*pi), sin(self.heading*pi)]])
        self.kf_init(self.kf_x, self.f_s, np.array([[1., 0.]]),
                     R_mult_x * gps_x_var,
                     Q_mult_x * Q_discrete_white_noise(2, 1./self.f_s, var=imu_x_var))
                     #custom_B=np.dot(self.discrete_b, x_b))

        # yaw axis kf config, 10hz, all units in degrees, ccw positive
        self.kf_yaw = KalmanFilter(dim_x=1, dim_z=1)
        self.kf_yaw.x = np.array([[0.0]])
        self.kf_init(self.kf_yaw, self.f_s, np.array([[1.]]),
                     R_mult_yaw * tan_var,
                     Q_mult_yaw * imu_yaw_var,
                     custom_F = np.array([[1.]]),
                     custom_B = np.array([[1/self.f_s]]))

        self.kf_int = KalmanFilter(dim_x=1, dim_z=1)
        self.kf_int.x = np.array([[0.0]])
        self.kf_init(self.kf_int, self.f_s, np.array([[1.]]),
                     R_mult_yaw * tan_var,
                     Q_mult_yaw * imu_yaw_var,
                     custom_F = np.array([[1.]]),
                     custom_B = np.array([[1/self.f_s]]))

        # time synchronizer for simultaneous sensor reading
        self.imu_sub = Subscriber(self, Imu, "/imu_raw", qos_profile=10) #qos profile always 10
        self.rpm_sub = Subscriber(self, RPM, "/rpm_raw", qos_profile=10) 
        self.time_sync = ApproximateTimeSynchronizer([self.imu_sub, self.rpm_sub],
                                                     10, 
                                                     0.01)

        self.time_sync.registerCallback(self.kf_update)

        # GPS Fusion
        self.gps_sub = Subscriber(self, GPS, "/gps_raw", qos_profile = 10)
        self.gps_fusion = ApproximateTimeSynchronizer([self.imu_sub, self.gps_sub],
                                                      10,
                                                      0.01)
        self.gps_fusion.registerCallback(self.gps_callback)
        self.ORIGIN_X = 64.8417 #north-south direction, latitude
        self.ORIGIN_Y = -30.2358 #east west-direction, longitude
        self.gps_x = self.ORIGIN_X
        self.gps_y = self.ORIGIN_Y
        # calibrate origin, pull first valid point as origin
        self.calibrated = False;
        self.dist_accu = 0.
        self.heading_accu = 0.
        # inert angle compare to true north, calculated by origin-waypoint pair
        self.heading_correction = -9.31 # degrees

    def kf_init(self, kf, f_s, custom_H, custom_R, 
                custom_Q, custom_F=None, custom_B=None):
        '''default: dt double integrator F=ma process 
            initial covariance set to identity
        '''
        if custom_F is None:
            kf.F = np.array([[1., 1./f_s],[0., 1.]])
        else:
            kf.F = custom_F
        if custom_B is None:
            kf.B = np.array([[1./(f_s*f_s*2.)],[1./f_s]]) # imu input
        else:
            kf.B = custom_B
        kf.H = custom_H
        kf.R = custom_R
        kf.Q = custom_Q

    def kf_update(self, imu_msg, rpm_msg):
        # self.get_logger().info('Fast Kalman updating')
        try:
            assert imu_msg.header.stamp == rpm_msg.header.stamp
        except AssertionError:
            # self.get_logger().info("Time stamp mismatch")
            pass
        finally:
            u_x = imu_msg.linear_acceleration.x - imu_x_mean
            u_psi = imu_msg.angular_velocity.z - imu_yaw_mean

            # only integrating angular z, no measurement
            self.kf_int.predict(u=np.array([[u_psi]]))
            
            # fast kf publish
            self.kf_localx.predict(u=np.array([[u_x]]))
            vel_meas = rpm_msg.derivedms - ms_mean
            self.kf_localx.update(vel_meas)
            
            x_fast_msg = XFiltered()
            x_fast_msg.header.stamp = self.get_clock().now().to_msg()
            x_fast_msg.header.frame_id = 'body' 
            x_fast_msg.xpos = float(self.kf_localx.x[0])
            x_fast_msg.xvel = float(self.kf_localx.x[1])
            x_fast_msg.yaw = float(self.kf_int.x[0])
            self.fast_pub.publish(x_fast_msg)
            # self.get_logger().info('Kalman X Updated')

    def gps_callback(self, imu_msg, gps_msg):
        # self.get_logger().warning('GPS Fusion Updating')
        if (not (self.calibrated)):
            self.gps_x = math.copysign(gps_msg.latmin, gps_msg.latdeg)
            self.gps_y = math.copysign(gps_msg.longmin, gps_msg.longdeg)
            self.ORIGIN_X = self.gps_x
            self.ORIGIN_Y = self.gps_y
            self.calibrated = True;
        # get new gps reading
        new_x = math.copysign(gps_msg.latmin, gps_msg.latdeg) # north-south, latitude
        new_y = math.copysign(gps_msg.longmin, gps_msg.longdeg) # east-west, longitude

        # crude distance calculation. 
        # swap out for haversine formula if lacking accuracy
        x_dist = approx_distance_lat(self.gps_x, new_x)
        y_dist = approx_distance_lon(self.gps_y, new_y)
        dist_travelled = math.sqrt(x_dist ** 2 + y_dist ** 2)
        self.dist_accu += dist_travelled

        # heading measurement based on gps difference
        # again, counter clock wise is positive, so flipping y direction
        # when going north
        try:
            if (self.heading % 1 == 0):
                # heading_meas = degrees(atan(-y_dist / x_dist))
                heading_meas = degrees(atan(-(new_y - self.ORIGIN_Y)/ (new_x - self.ORIGIN_X)))
            else:
                # heading_meas = degrees(atan(x_dist / y_dist))
                heading_meas = degrees(atan((new_x - self.ORIGIN_X)/(new_y - self.ORIGIN_X)))
        except ZeroDivisionError:
            heading_meas = 0
        finally:
            heading_meas = heading_meas - self.heading_correction

        u_x = imu_msg.linear_acceleration.x - imu_x_mean
        u_psi = imu_msg.angular_velocity.z - imu_yaw_mean

        self.kf_x.predict(u=np.array([[u_x]]))
        self.kf_x.update(self.dist_accu)

        self.kf_yaw.predict(u=np.array([[u_psi]]))
        self.kf_yaw.update(heading_meas)

        # publish updated x and yaw estimate
        x_msg = XFiltered()
        x_msg.header.stamp = self.get_clock().now().to_msg()
        x_msg.header.frame_id = 'body' 
        x_msg.xpos = float(self.kf_x.x[0])
        x_msg.xvel = float(self.kf_x.x[1])
        x_msg.weighted_x_pos = float(self.kf_localx.x[0] * (1.-weight) + self.kf_x.x[0] * weight)
        x_msg.yaw = float(self.kf_yaw.x[0])
        x_msg.yawvel = float(u_psi)

        # debug values
        x_msg.debug_gps_x = float(x_dist)
        x_msg.debug_gps_y = float(y_dist)
        x_msg.debug_tan_meas = float(heading_meas)
        x_msg.debug_gps_accu_x = float(self.dist_accu)
        self.state_pub.publish(x_msg)


        # update distance measurement, correct for bias
        self.gps_x = new_x - gps_x_mean
        self.gps_y = new_y - gps_y_mean

    def heading_update(self, heading_msg):
        # only updates when there's a heading change
        if (self.heading != heading_msg.heading):
            self.heading = heading_msg.heading
            self.kf_x.x[0] = 0
            self.dist_accu = 0
            self.kf_localx.x[0] = 0
            # redefines origin for heading measurement
            self.calibrated = False

        

def main(args=None):
    rclpy.init(args=args)

    kalman = KalmanNode()

    rclpy.spin(kalman)

    #rpm_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()


