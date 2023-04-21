# kalman filter constants
# calculated by Matlab

imu_x_mean = 0.0264
imu_y_mean = -0.08387
imu_psi_mean = -1.548
rpm_mean = 0
gps_mean = 0
imu_x_var = 3.211e-5
imu_y_var = 1.496e-5
imu_psi_var = 0.005589
rpm_cov = 0
gps_cov = 0
tan_cov = max(imu_x_var, imu_y_var)
