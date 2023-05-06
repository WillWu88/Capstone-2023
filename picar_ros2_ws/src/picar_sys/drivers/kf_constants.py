# kalman filter constants
# calculated by Matlab
import math

# tuning: section
Q_mult_x = 1.
R_mult_x = 1.
Q_mult_y = 1.0
R_mult_y = 1.0
imu_x_mult = 1500
imu_y_mult = 19000
gps_x_mult = 0.05
gps_y_mult = 0.015
ms_x_mult = 0.5
ms_y_mult = 0.5
local_ms_mult = 1
local_imu_x_mult = 1

imu_x_mean = 0.0264
imu_y_mean = -0.0839
imu_x_var = 3.211e-5 * imu_x_mult
imu_y_var = 1.711e-6 * imu_y_mult
ms_mean = 0.
ms_var = 0.0092
gps_x_mean = 0.
gps_x_var = 4.350e-5 * gps_x_mult
gps_y_mean = 0.
gps_y_var = 1.174e-4 * gps_y_mult
tan_mean = 0.
tan_var = 0.0038

# helper constants
deg_rad_conv = 0.0175 # pi / 180
