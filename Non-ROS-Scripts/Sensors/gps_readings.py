# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple GPS module demonstration.
# Will wait for a fix and print a message every second with the current location
# and other details.
import time
import board
import serial
import numpy as np;
import math
from scipy.io import savemat
import sys

from datetime import date
import adafruit_gps


uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)  # Use UART/pyserial
# gps = adafruit_gps.GPS_GtopI2C(i2c, debug=False)  # Use I2C interface
gps.send_command(b"PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0")
# Turn on just minimum info (RMC only, location):
# gps.send_command(b'PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
# Turn off everything:
# gps.send_command(b'PMTK314,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
# Turn on everything (not all of it is parsed!)
# gps.send_command(b'PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0')

gps.send_command(b"PMTK220,100")
last_print = time.monotonic()
log_data = np.zeros((2,50))
'''
index_dict = {
    "x_pos": 0,
    "x_velocity": 1,
    "y_pos": 2,
    "y_velocity": 3
}
'''

index_dict = {
    "long": 0,
    "lat": 1
}

sample_count = 0

if __name__ == "__main__":
    sample_count = 0
    sample_num = int(input("# of data > "))
    log_data = np.zeros((2, sample_num))

    print("Collecting data now...")
    while sample_count < sample_num:
    # Make sure to call gps.update() every loop iteration and at least twice
    # as fast as data comes from the GPS unit (usually every second).
    # This returns a bool that's true if it parsed new data (you can ignore it
    # though if you don't care and instead look at the has_fix property).
        gps.update()
    # Every second print out current location details if there's a fix.
        current = time.monotonic()
        if current - last_print >= 0.1:
            last_print = current
            if not gps.has_fix:
            # Try again if we don't have a fix yet
                print("Waiting for fix...")
                continue
        # We have a fix! (gps.has_fix is true)
        # Print out details about the fix like location, date, etc.
            print("Collecting")
            print(sample_count)
            log_data[index_dict["long"], sample_count] = gps.longitude_minutes
            log_data[index_dict["lat"], sample_count] = gps.latitude_minutes

            sample_count += 1

    output_data = {"GPS_readings": log_data}
    date_str = date.today()
    savemat("./Data/GPS_readings_"+date_str.strftime("%b_%d_%Y")+".mat", output_data)
'''
    except KeyboardInterrupt:
        output_data = {"GPS_readings": log_data}
        date_str = date.today()
        savemat("./Data/GPS_readings_"+date_str.strftime("%b_%d_%Y")+".mat", output_data)
'''

