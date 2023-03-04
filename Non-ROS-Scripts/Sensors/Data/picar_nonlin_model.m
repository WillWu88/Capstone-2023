%% Pi Car Non-Linear Dynamics Model
% parameter helper script
% by Will Wu, Payton Irwin
clear, clc, close all;

%% PiCar Param definition

mass_total = (1545.1 + 395.5 + 187.3 + 210.5 + 82.9 + 87.8 + 59.23...
    + 58.84)/1000;

% distance measurements
cg_front_ax = 18.3/100;
cg_back_ax = 10.5/100;
total_lenght = 42/100;
total_width = 32.5/100;

% tyre slip
back_wheel_s = 0.05; % percent
front_wheel_s = 0.02;

% moment of inertia
J = 0.0359; % kg*m^2

% motor param
total_power = 42.24/1000; % watt
tau_multiplier = 9.5488 * total_power; % divide by RPM to get engine torque
gear_ratio = 16/(3*103);

% system ID param, sourced from 
% https://www.politesi.polimi.it/bitstream/10589/137501/1/Tesi Ravizzoli Carlo.pdf

% tyre params
c_x = 17; %N/rad
c_y = 17.81;
wheel_rad_r = 101/1000; % rear wheel radius, meters
wheel_rad_f = 80/1000; % front wheel radius, meters

%% Numerical Simulation

x_0 = [0 0 0]'; % initial condition, zero speed
f_s = 100; % 100Hz update rate
t = 0:1/f_s:10-1/f_s; % 10s simulation, sampling at 100Hz for dt systems



% simulation, crude for loop for now
% [t,y] = ode45(@(v_x, v_y, v_z) state_space([v_x v_y v_z]', [0 0]), t, x_0);

% Input: 3s engine step input from t=2-5, 700 RPM (around 20%)
tau_20 = tau_multiplier / (700 * gear_ratio); % 6:1 gear ratio
tau_in = tau_20*(heaviside(t-2) - heaviside(t-5));
steer_angle = 0 * t;    

u = [tau_in; steer_angle]';

y = zeros(length(t), length(x_0));
for i=1:length(t)-1
    if (i == 1)
        x_curr = x_0;
    else
        x_curr = y(i,:);
    end
    y(i+1,:) = state_space(x_curr, u(i,:));
end

%% function declaration, dynamics model

function force = fx_front(c_x, s_i)
    force = c_x * s_i;
end

function force = fx_rear(r_wheel, tau)
    force = tau/r_wheel;
end

function force = fy_front(c_y, a, states, delta)
    v_x = states(1);
    v_y = states(2);
    r_z = states(3);
    
    if (v_x == 0)
        alpha = delta;
    else
        alpha = delta - atan((v_y + a*r_z)/v_x);
    end
    force = c_y * alpha; 
end

function force = fy_rear(c_y, b, states)
    v_x = states(1);
    v_y = states(2);
    r_z = states(3);
    if (v_x == 0)
        alpha = 0;
    else
       alpha = - atan((v_y - b*r_z)/v_x);
    end
    force = c_y * alpha;
end

function x_dot = state_space(x, u)

    % paste physical params here till better solutions than global variables
    % are found
    mass_total = (1545.1 + 395.5 + 187.3 + 210.5 + 82.9 + 87.8 + 59.23...
        + 58.84)/1000;
    
    % distance measurements
    cg_front_ax = 18.3/100;
    cg_back_ax = 10.5/100;
    
    % tyre slip
    front_wheel_s = 0.02;
    
    % moment of inertia
    J = 0.0359; % kg*m^2
    
    % tyre params
    c_x = 17; %N/rad
    c_y = 17.81;
    wheel_rad_r = 101/1000; % rear wheel radius, meters

    % state decomp
    v_x = x(1);
    v_y = x(2);
    r_z = x(3);
    tau = u(1);
    delta = u(2);

    % forces calculation
    f_x_fl = fx_front(c_x, front_wheel_s);
    f_x_fr = fx_front(c_x, front_wheel_s);
    f_x_rr = fx_rear(wheel_rad_r, tau);
    f_x_rl = fx_rear(wheel_rad_r, tau);

    f_y_fl = fy_front(c_y, cg_front_ax, x, delta);
    f_y_fr = fy_front(c_y, cg_front_ax, x, delta);
    f_y_rl = fy_rear(c_y, cg_back_ax, x);
    f_y_rr = fy_rear(c_y, cg_back_ax, x);

    x_dot(1) = v_y * r_z + 1/mass_total*((f_x_fl + f_x_fr)*cos(delta)...
                                        - (f_y_fl + f_y_fr)*sin(delta)...
                                        + f_x_rl + f_x_rr);
    x_dot(2) = -v_x * r_z + 1/mass_total*((f_x_fl + f_x_fr)*sin(delta)...
                                          - (f_y_fl + f_y_fr)*cos(delta)...
                                          + f_y_rl + f_y_rr);
    x_dot(3) = 1/J*( cg_front_ax * ((f_x_fl + f_x_fr) * sin(delta) ...
                                    + (f_y_fl + f_y_fr) * cos(delta))...
                     - cg_back_ax * (f_y_rr + f_y_rl));
end

