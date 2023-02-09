import RPi.GPIO as IO
import math
from board import SCL,SDA
import busio
from adafruit_pca9685 import PCA9685
import time
import adafruit_motor.servo
# from rpm_sensor import *

def Servo_Motor_Initialization():
   i2c_bus = busio.I2C(SCL,SDA)
   pca = PCA9685(i2c_bus)
   pca.frequency = 100
   return pca

def Motor_Start(pca):
   x = input("Press and hold ez button. When RED LED turns red wait 3 seconds.")
   Motor_Speed(pca, 1)
   time.sleep(3)
   Motor_Speed(pca, 0)
   Motor_Speed(pca, -1)
   time.sleep(3)
   Motor_Speed(pca, 0)
   time.sleep(3)

def Motor_Speed(pca,percent):
   #converts a -1 to 1 value to 16-bit duty cycle
   speed = ((percent) * 3276) + 65535 * 0.15
   pca.channels[15].duty_cycle = math.floor(speed)

#initialization
pca = Servo_Motor_Initialization()

arm_state = input("Armed? (y/n)> ")
if (arm_state !="y"):
    Motor_Start(pca)

while True:
    command = input("Stop? (y/n)> ")
    if (command == "y"):
        Motor_Speed(pca,0)
        break

    print("running motor")
    Motor_Speed(pca, 0.2)

    '''
    curr_pin_val = IO.input(GPIO_num)
    if not(curr_pin_val) and last_val:
        stop = time.perf_counter();
        raw_reading = rpm_filter.CalcRaw(start, stop)
        print("Detected!")
        print("Raw RPM reading is:"+ str(raw_reading))
        print("Filtered reading is: "+ str(rpm_filter.CalcFilter()))
        last_val = curr_pin_val
        start = stop
    else:
        last_val = curr_pin_val
        '''
