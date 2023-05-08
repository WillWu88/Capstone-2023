# kalman filter constants
# calculated by Matlab
import math

# TUNING SECTION:

# local fast x-axis kf
Q_mult_local_x = 1.
local_ms_mult = 1.5
# global x-axis kf
Q_mult_x = 0.01
R_mult_x = 1000.
# global yaw kf
Q_mult_yaw = 1.0
R_mult_yaw = 1.0

# process input calibration
imu_x_mean = 0.0264
imu_x_var = 3.211e-5 
imu_yaw_mean = -1.5488
imu_yaw_var = 0.0056
ms_mean = 0.
ms_var = 0.0092
gps_x_mean = 0.
gps_x_var = 4.350e-5 
gps_y_mean = 0.
gps_y_var = 1.174e-4
tan_mean = 0.
tan_var = 0.0038

# helper constants
deg_rad_conv = 0.0175 # pi / 180

# weighted consensus
weight = 0.55
