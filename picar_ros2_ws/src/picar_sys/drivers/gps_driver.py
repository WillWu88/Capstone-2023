import time
import board
import serial

import adafruit_gps
from drivers.car_param import *

class GPSDriver():

    def __init__(self):
        self.index_dict = {
            "lat_deg": 0,
            "lat_min": 1,
            "long_deg":2,
            "long_min": 3
            
        }
        self.data = [0]*len(self.index_dict)
        self.uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
        self.gps = adafruit_gps.GPS(self.uart, debug=False)  # Use UART/pyserial
        self.gps_init()

    def gps_init(self):
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        self.gps.send_command(b"PMTK220,100")  
    
    def update(self):
        self.gps.update()
        if not self.gps.has_fix:
            self.data[self.index_dict['lat_deg']] = 38.
            self.data[self.index_dict['lat_min']] = ORIGIN_X
            self.data[self.index_dict['long_deg']] = -90.0
            self.data[self.index_dict['long_min']] = ORIGIN_Y
        else:
            self.data[self.index_dict['lat_deg']] = float(self.gps.latitude_degrees)
            self.data[self.index_dict['lat_min']] = float(self.gps.latitude_minutes)
            self.data[self.index_dict['long_deg']] = float(self.gps.longitude_degrees)
            self.data[self.index_dict['long_min']] = float(self.gps.longitude_minutes)
        

