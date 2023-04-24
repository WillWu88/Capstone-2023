import numpy as np
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
from kf_constants import *
from car_param import *


def kf_init(kf, f_s, custom_H, custom_R, custom_Q):
    '''default: dt double integrator F=ma process 
         initial covariance set to identity
    '''
    kf.F = np.array([[1., 1/f_s],[0., 1.]])
    kf.B = np.array([[1./(f_s*f_s*2.)],[1./f_s]]) # imu input
    kf.H = custom_H
    kf.R = custom_R
    kf.Q = custom_Q

f_s = 100.0
kf_x = KalmanFilter(dim_x=2, dim_z=1)
kf_init(kf_x, f_s, np.array([[0., 1.]]), np.array([[rpm_cov]]), 
                Q_discrete_white_noise(2, 1./f_s, var=imu_x_var))
kf_x.inv = np.reciprocal


v_x_meas = 1.0
u_x = 1.0

while True:
    v_x_meas = v_x_meas + 0.5
    kf_x.predict(u=u_x)
    kf_x.update(v_x_meas)
