#Reading of 0 means magnet detected,
#reading of 1 means no magnet detected

import RPi.GPIO as IO
import time
import sys
import argparse
import busio
import smbus
from time import sleep
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import math

IO.setwarnings(False)
IO.setmode(IO.BCM)

GPIO_num = 16
IO.setup(GPIO_num,IO.IN,IO.PUD_UP)
last_val = IO.input(GPIO_num)

while True:
    curr_pin_val = IO.input(GPIO_num)
    if not(curr_pin_val) and last_val:
        print("Detected!")
        last_val = curr_pin_val
    else:
        last_val = curr_pin_val
