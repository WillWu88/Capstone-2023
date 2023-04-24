import math
from board import SCL,SDA
import busio
from adafruit_pca9685 import PCA9685
import time
import adafruit_motor.servo

class MotorDriver():
    ''' WARNING!! This driver assumes that motor is armed.
        - Use command_motor.py in Non-ROS-Scripts to arm and test
    '''
    def __init__(self):
        self.i2c_bus = busio.I2C(SCL,SDA)
        self.pca = PCA9685(self.i2c_bus)
        self.pca.frequency = 100

    def Motor_Speed(self, percent):
        #converts a -1 to 1 value to 16-bit duty cycle
        speed = ((percent) * 3276) + 65535 * 0.15
        self.pca.channels[15].duty_cycle = math.floor(speed)
