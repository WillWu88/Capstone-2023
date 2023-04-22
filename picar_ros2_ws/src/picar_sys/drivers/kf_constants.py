# kalman filter constants
# calculated by Matlab
import math

# tuning: section
Q_mult_x = 5000.0
R_mult_x = 0.005
Q_mult_psi = 1.0
R_mult_psi = 10.0

imu_x_mean = 0.0264
imu_y_mean = -0.0839
imu_x_var = 3.211e-5
ms_mean = 0.
ms_var = 0.0092
gps_mean = 0.
gps_cov = 0.
imu_psi_mean = -1.549
imu_psi_var = 1.711e-6
tan_mean = 0.
tan_var = 0.0038

# helper constants
deg_rad_conv = 0.0175 # pi / 180
