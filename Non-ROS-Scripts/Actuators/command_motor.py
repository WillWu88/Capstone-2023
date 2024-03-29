import math
from board import SCL,SDA
import busio
from adafruit_pca9685 import PCA9685
import time
import adafruit_motor.servo

def Servo_Motor_Initialization():
   i2c_bus = busio.I2C(SCL,SDA)
   pca = PCA9685(i2c_bus)
   pca.frequency = 100
   return pca

def Motor_Start(pca):
   x = input("Press and hold the esc button until the red light turns off. Wait for redlight to flush once and immediately press enter> ")
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
   print(speed/65535)

#initialization
pca = Servo_Motor_Initialization()

arm_state = input("Armed? (y/n)> ")
if (arm_state !="y"):
    Motor_Start(pca)

while True:
    command = input("Stop? (y/n/val)> ")
    if (command == "y"):
        Motor_Speed(pca,0)
        break

    Motor_Speed(pca, float(command))
