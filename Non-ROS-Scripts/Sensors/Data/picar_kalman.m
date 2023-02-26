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

% lables
acc_x = 2;
acc_y = 3;
acc_z = 4;
gyro_x = 5;
gyro_y = 6;
gyro_z = 7;

% all data are sampled at 1000Hz for 10 seconds
f_s = 1000;
time_stat = 0:1/f_s:10-1/f_s;
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

%% statiscal analysis

% distribution analysis
figure, histogram(stationary(acc_x,:)), title('X Acc Distribution');
figure, histogram(stationary(acc_y,:)), title('Y Acc Distribution');
figure, histogram(stationary(acc_z,:)), title('Z Acc Distribution');

% gyro readings in deg/s
sensor_mean = mean(stationary(acc_x:gyro_z,:),2);

% starting Kalman Q & R values
sensor_cov = cov(transpose(stationary(acc_x:gyro_z,:)));
sensor_var = diag(sensor_cov);

