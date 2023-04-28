import time
import busio
from board import SCL, SDA
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

class ServoDriver():
    
    def __init__(self):
        self.pca = PCA9685(busio.I2C(SCL, SDA))
        self.pca.frequency = 100
        channel_num = 14
        self.servo_actuator = servo.Servo(self.pca.channels[channel_num])
        self.maxAngle = 30
        self.setAngle(0)
       
    def progressiveSet(self, newAngle):
        target = self.turnAngleToRCAngle(newAngle)
        while self.currAngle != newAngle:
            if(self.currAngle > newAngle):
                self.currAngle -= 1
            if(self.currAngle < newAngle):
                self.currAngle += 1
            self.servo_actuator.angle = int(target)
            time.sleep(0.01)

    def turnAngleToRCAngle(self, angle):
        angle = angle + self.maxAngle + 3
        if(angle == self.maxAngle):
            angle = 90
        elif(angle < self.maxAngle):
            offset = (angle / self.maxAngle) * 55
            offset = 55 - offset
            angle = 90 + offset
        elif(angle > self.maxAngle):
            offset = ((angle - self.maxAngle) / self.maxAngle) * 55
            angle = 90 - offset
        return(angle)

    def setAngle(self, newAngle):
        target = self.turnAngleToRCAngle(newAngle)
        self.servo_actuator.angle = int(target)

