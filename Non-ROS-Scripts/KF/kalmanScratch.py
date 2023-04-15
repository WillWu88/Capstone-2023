import numpy as np
import scipy as sp


class KalmanFilter():

    def __init__(self, x_0, f_s, A=None, B=None, C=None, D=None, p_0=None, Q_k, R_k):
        self.f_s = f_s
        
        if (A == None):
            # default: discrete time double integrator
            self.A = np.array([[1, 1/self.f_s],[0,1]])
        else:
            self.A = A

        if (B == None):
            # default: single process input on second state
            self.B = np.array([[1/(2*self.f_s*self.f_s)], [1/self.f_s]])
        else:
            self.B = B
        
        if (C == None):
            # default: single measurement input on first state
            self.C = np.array([1, 0])
        else:
            self.C = C

        if (D == None):
            # default: zero single input
            self.D = np.zeros((1,1))
        else:
            self.D = D
        
        if (p_0 == None):
            # default: zero single input
            self.p_0 = np.eye(self.A.ndim)
        else:
            self.p_0 = p_0

        self.Q_k = Q_k
        self.R_k = R_k
        self.state = x_0
        self.cov_mat = np.zeros(self.Q_k.shape)
        
        self.temp_state = self.x_0
        self.temp_cov = self.cov_mat
        self.k_gain = np.zeros((self.C.ndim, self.C.ndim))
        


    def predict(self, u_process):
        pass

    def update(self, y_meas):
        pass

    def readState(self, idx):
        if (idx >= self.state.ndim):
            return 0
