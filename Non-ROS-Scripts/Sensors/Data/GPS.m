%% GPS Analysis
% by Will Wu
clear, clc, close all;


%% import all data

% labels
longitude = 1;
latitude = 2;

% GPS data sets, stationary
point1_pre_powercycle = load('org_pre.mat');
point1_pre_powercycle = point1_pre_powercycle.GPS_readings;
point1_post_powercycle = load('org_post.mat');
point1_post_powercycle = point1_post_powercycle.GPS_readings;
point2_pre_powercycle = load('mid_pre.mat');
point2_pre_powercycle = point2_pre_powercycle.GPS_readings;
point2_post_powercycle = load('mid_post.mat');
point2_post_powercycle = point2_post_powercycle.GPS_readings;
point3_pre_powercycle = load('final_pre.mat');
point3_pre_powercycle = point3_pre_powercycle.GPS_readings;
point3_post_powercycle = load('final_post.mat');
point3_post_powercycle = point3_post_powercycle.GPS_readings;

%% Plotting

% latitude drift plot
figure, hold on;
plot (point1_pre_powercycle(2,:))
plot (point1_post_powercycle(2,:))
plot (point2_pre_powercycle(2,:))
plot (point2_post_powercycle(2,:))
plot (point3_pre_powercycle(2,:))
plot (point3_post_powercycle(2,:))
xlabel('Time'), ylabel('GPS Minute Readout');
title('Latitude drift before/after power cycle')

legend('1 pre','1 post','2 pre', '2 post','3 pre', '3 post')

% longitude drift plot
figure, hold on;
plot (point1_pre_powercycle(1,:))
plot (point1_post_powercycle(1,:))
plot (point2_pre_powercycle(1,:))
plot (point2_post_powercycle(1,:))
plot (point3_pre_powercycle(1,:))
plot (point3_post_powercycle(1,:))
xlabel('Time'), ylabel('GPS Minute Readout');
title('Longitude drift before/after power cycle')

legend('1 pre','1 post','2 pre', '2 post','3 pre', '3 post')