import numpy as np
import math
import time

class PidDriver():

    def __init__(self, Ki, Kp, Kd, delta, sat_val):
        self.curr_state = 0.
        self.setpoint = 0.
        self.e1 = 0.
        self.e2 = 0.
        self.e3 = 0.
        self.u_curr = 0.
        self.u_last = 0.
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.delta = delta
        self.sat_val = sat_val

    def error_calc(self):
        self.e1 = self.setpoint - self.curr_state

    def pid_calc(self):
        mult_e1 = self.Kp + self.Ki*self.delta + self.Kd/self.delta
        mult_e2 = -self.Kp - 2*self.Kd/self.delta
        mult_e3 = self.Kd/self.delta
        self.u_curr = self.saturation(self.u_last + 
                                      mult_e1*self.e1 + 
                                      mult_e2*self.e2 + mult_e3*self.e3)
        return self.u_curr

    def update(self):
        self.e2 = self.e1
        self.e3 = self.e2
        self.u_last = self.u_curr

    def saturation(self, u):
        # allow for negative inputs
        if (abs(u) >= sat_val):
            return math.copysign(sat_val, u)
        else:
            return u

