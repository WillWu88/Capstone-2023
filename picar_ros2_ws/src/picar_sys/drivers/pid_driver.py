import numpy as np
import time

class PidDriver():

    def __init__(self):
        selk.Kp = 0
        self.Ki = 0
        self.Kd = 0
        self.e1 = 0
        self.e2  =0
        self.e3 = 0
        self.u_last = 0
        self.u_curr = 0
        self.delta = 0.05
        
    def pid_calc(self):
        self.mult_e1 = self.Kp + self.Ki*self.delta+ self.Kd/self.delta
        self.mult_e2 = -self.Kd - 2*self.Kp/self.delta
        self.mult_e3 = self.Kd/self.delta
        u_curr = self.u_last +  self.mult_e1*self.e1 + self.mult_e2*self.e2 + self.mult_e3*self.e3
        return u_curr

    def update(self):
        self.e1 = 0 # change this
        self.e2 = self.e1
        self.e3 = self.e2
        self.u_last = self.u_curr

