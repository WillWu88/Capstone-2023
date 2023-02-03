# Credit: http://www.electronicwings.com
import smbus					#import SMBus module of I2C
from time import sleep          #import
from imu_param import *      #import IMU setup params
import numpy as np;
from scipy import savemat
from datetime import date

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47


def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, ONE_K_HZ)
    #gyro sampling at 1kHz
	
	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, INPUT_DISABLED_MAX_FS)
	
	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, GYRO_MIN_RANGE)
	
	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

label_dict = {
        "acc_x": 0,
        "acc_y": 1,
        "acc_z": 2,
        "gyro_x": 3,
        "gyro_y": 4,
        "gyro_z": 5
}

if __name__ == "__main__":
        # log user-specified amount of sensor data
        print (" Reading Data of Gyroscope and Accelerometer")
        sample_num = (" Input # of data here: >>> ")

        log_data = np.zeros((7,sample_num))
        log_data[1,:] = np.arange(sample_num) + 1;  #index row

        sample_count = 0
        while sample_count < 1000:

	        #Read Accelerometer and Gyro value, then convert
	        log_data[label_dict["acc_x"], sample_count] = read_raw_data(ACCEL_XOUT_H)/16384.0
	        log_data[label_dict["acc_y"], sample_count] = read_raw_data(ACCEL_YOUT_H)/16384.0
	        log_data[label_dict["acc_z"], sample_count] = read_raw_data(ACCEL_ZOUT_H)/16384.0

	        #Read Gyroscope raw value
	        log_data[label_dict["gyro_x"], sample_count] = read_raw_data(GYRO_XOUT_H)/131.0
	        log_data[label_dict["gyro_y"], sample_count] = read_raw_data(GYRO_YOUT_H)/131.0
	        log_data[label_dict["gyro_z"], sample_count] = read_raw_data(GYRO_ZOUT_H)/131.0

                sample_count = sample_count + 1

	        #print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az)
	        #sleep(1)

       output_data = {"acc_gyro_sample": log_data}
       date_str = date.today() #system time stamp
       savemat("IMU_data_"+date_str.strftime("%b_%d_%Y") +".mat", output_data)
