# Credit: http://www.electronicwings.com
import smbus					#import SMBus module of I2C
from time import sleep          #import
from drivers.imu_param import *      #import IMU setup params
import numpy as np;
from scipy.io import savemat
from datetime import date


class IMUDriver():

    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.device_address = 0x68   # device address
        self.MPU_Init()
        self.index_dict = {
            "acc_x": 0,
            "acc_y": 1,
            "acc_z": 2,
            "gyro_x": 3,
            "gyro_y": 4,
            "gyro_z": 5
        }
        self.data = [0] * len(self.index_dict)

    def MPU_Init(self):
    	#write to sample rate register
    	self.bus.write_byte_data(self.device_address, SMPLRT_DIV, ONE_K_HZ)
        #gyro sampling at 1kHz
    	
    	#Write to power management register
    	self.bus.write_byte_data(self.device_address, PWR_MGMT_1, 1)
    	
    	#Write to Configuration register
    	self.bus.write_byte_data(self.device_address, CONFIG, INPUT_DISABLED_MAX_FS)
    	
    	#Write to Gyro configuration register
    	self.bus.write_byte_data(self.device_address, GYRO_CONFIG, GYRO_MIN_RANGE)
    	
    	#Write to interrupt enable register
    	self.bus.write_byte_data(self.device_address, INT_ENABLE, 1)
    
    def read_raw_data(self, addr):
    	#Accelero and Gyro value are 16-bit
        high = self.bus.read_byte_data(self.device_address, addr)
        low = self.bus.read_byte_data(self.device_address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value

    def update(self):
        #Read Accelerometer and Gyro value, then convert
        self.data[self.index_dict["acc_x"]] = self.read_raw_data(ACCEL_XOUT_H)/16384.0
        self.data[self.index_dict["acc_y"]] = self.read_raw_data(ACCEL_YOUT_H)/16384.0
        self.data[self.index_dict["acc_z"]] = self.read_raw_data(ACCEL_ZOUT_H)/16384.0

        #Read Gyroscope raw value
        self.data[self.index_dict["gyro_x"]] = self.read_raw_data(GYRO_XOUT_H)/131.0
        self.data[self.index_dict["gyro_y"]] = self.read_raw_data(GYRO_YOUT_H)/131.0
        self.data[self.index_dict["gyro_z"]] = self.read_raw_data(GYRO_ZOUT_H)/131.0




if __name__ == "__main__":
    
    # log user-specified amount of sensor data
    sample_num = int(input(" Input # of data here: >>> "))
    imu = IMUDriver()

    sample_count = 0
    print("Collecting data now...")
    while sample_count < sample_num:
        sample_count += 1
        imu.update()
        print(imu.data[1])



