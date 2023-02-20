%% Sensor Noise Statistical Analysis
% Will Wu
clc, clear, close all;
load('RPM_Data_Feb_16_2023.mat')
%% RPM Sensor at 0.2 PWM

figure, hold on;
plot(RPM_sample(1,:));
plot(RPM_sample(2,:));
title('Raw vs Filtered RPM Reading')
legend('Raw', 'Filtered')
xlabel('Sample')
ylabel('RPM Reading')