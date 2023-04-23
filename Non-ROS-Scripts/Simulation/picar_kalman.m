%% PiCar Kalman Filter Helper Script
% by Will Wu
clear, clc, close all

%% Import data
stationary = load('IMU_stationary.mat');
stationary = stationary.acc_gyro_sample;
x_jiggle = load('IMU_x_jiggle.mat');
x_jiggle = x_jiggle.acc_gyro_sample;
y_jiggle = load('IMU_y_jiggle.mat');
y_jiggle = y_jiggle.acc_gyro_sample;
rpm_20 = load('RPM_Data_Apr_21_2023.mat');
rpm_20 = rpm_20.RPM_sample;
m_s_20 = rpm_20(2,:)*pi*0.105/60;
gps = load('GPS_readings_Apr_23_2023.mat');
gps = gps.GPS_readings;


% lables
acc_x = 2;
acc_y = 3;
acc_z = 4;
gyro_x = 5;
gyro_y = 6;
gyro_z = 7;

longitude = 1;
latitude = 2;


% all data are sampled at 1000Hz for 10 seconds
f_s = 1000;
time_stat = 0:1/f_s:10-1/f_s;
atan_psi = atan(stationary(acc_y, :) ./ stationary(acc_x, :));
psi_rad = stationary(gyro_z,:) .*0.0175;

%% IMU Behaviroal Analysis

% jiggle data sets are data collected while shaking the IMU back and forth
% along a certain axis

% x jiggle
figure, hold on;
time_j = 0:1/f_s:1-1/f_s; % jiggle sampled for 1s at 1000Hz
plot(time_j, x_jiggle(acc_x, :));
plot(time_j, x_jiggle(acc_y, :));
plot(time_j, x_jiggle(acc_z, :));
legend('x','y','z'), xlabel('Time'),ylabel('Magnitude (m/s^2)');
title('Jiggling on X axis')

% y jiggle
figure, hold on;
plot(time_j, y_jiggle(acc_x, :));
plot(time_j, y_jiggle(acc_y, :));
plot(time_j, y_jiggle(acc_z, :));
legend('x','y','z'), xlabel('Time'),ylabel('Magnitude (m/s^2)');
title('Jiggling on Y axis')

% stationary, linear acc as a time series
figure, hold on;
plot(time_stat, stationary(acc_x, :));
plot(time_stat, stationary(acc_y, :));
plot(time_stat, detrend(stationary(acc_z, :))); % note that z is detrended
legend('x','y','z'), xlabel('Time'),ylabel('Magnitude (m/s^2)');
title('Sensor Data at Stationary Equilibrium')

% RPM time series, 10000 samples
figure;
plot(rpm_20(2,:))
title('RPM Time Series')

figure, plot(m_s_20), title('m/s time series')

%% statiscal analysis

% distribution analysis
figure, histogram(stationary(acc_x,:)), title('X Acc Distribution');
figure, histogram(stationary(acc_y,:)), title('Y Acc Distribution');
figure, histogram(stationary(acc_z,:)), title('Z Acc Distribution');
figure, histogram(rpm_20(2,:)), title('RPM Distribution (20% PWM)');
figure, histogram(m_s_20), title('linear speed Distribution (20% PWM)')
figure, histogram(psi_rad), title('Yaw angular velocity (rad/s)')
figure, histogram(gps(longitude,:)), title('Longitude Distribution');
figure, histogram(gps(latitude,:)), title('Latitude Distribution');

% gyro readings in deg/s
sensor_mean = mean(stationary(acc_x:gyro_z,:),2);
rpm_mean = mean(rpm_20(2,:));
m_s_mean = mean(m_s_20);
psi_meas_mean = mean(atan_psi);
psi_rad_mean = mean(psi_rad);
gps_mean = mean(gps,2);

% starting Kalman Q & R values
sensor_cov = cov(transpose(stationary(acc_x:gyro_z,:)));
sensor_var = diag(sensor_cov);  
rpm_cov = cov(rpm_20(2,:));
m_s_cov = cov(m_s_20);
psi_cov = cov(atan_psi);
psi_rad_cov = cov(psi_rad);
gps_cov = cov(gps');

%% Kalman filter setup
f_s = 100; %Hz
delta_t = 1/f_s;
A_kf = [1 delta_t;0 1];
b_kf = [delta_t^2/2; delta_t];
c_x = eye(2);
d_x = zeros(2,1);

t = 0:delta_t:((length(time_stat)-1)/f_s);
a_x_in = [t' transpose(stationary(acc_x, :))];

rpm_in = zeros(size(t'));
gps_in = zeros(size(t'));

meas_x_in = [t' gps_in rpm_in];

