#Reading of 0 means magnet detected,
#reading of 1 means no magnet detected

import RPi.GPIO as IO
import time
import sys
import argparse
import busio
import smbus
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import math




class circ_buff:
    def __init__(self, size):
        self.size = size
        self.circ = [0] * self.size
        # zero out initial buffer, fixed sized
        self.write_ptr = 0

    def updateBuffer(self, new_val):
        self.circ[self.write_ptr % self.size] = new_val #insert new val based on ptr
        self.write_ptr += 1

    def CalcRaw(self, start_time, stop_time):
        raw_rpm = 60/(stop_time - start_time)
        self.updateBuffer(raw_rpm)
        return raw_rpm
        
    def CalcFilter(self):
        # moving average filter
        filter_sum = 0;
        for elements in self.circ:
            filter_sum += elements
        return filter_sum/self.size



IO.setwarnings(False)
IO.setmode(IO.BCM)

GPIO_num = 16
IO.setup(GPIO_num,IO.IN,IO.PUD_UP)
last_val = IO.input(GPIO_num)
start = time.perf_counter()
rpm_filter = circ_buff(5)
'''

while True:
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



