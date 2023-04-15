import time
import board
import serial

import adafruit_gps

class GPSDriver():

    def __init__(self,size):
        self.size = size
        self.index_dict = {
            "lat_deg": 0,
            "lat_min": 1,
            "long_deg":2,
            "long_min": 3
            
        }
        self.data = [0]*len(self.index_dict)
        self.gps_init()
        self.uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
        self.gps = adafruit_gps.GPS(uart, debug=False)  # Use UART/pyserial

    def gps_init(self):
        # import serial
        # Create a GPS module instance.
        # Turn on the basic GGA and RMC info (what you typically want)
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        # Set update rate to once a second (1hz) which is what you typically want.
        self.gps.send_command(b"PMTK220,1000")  
    
    def update(self):
        self.gps.update()
        if not gps.has_fix:
            self.data[self.index_dict["lat_deg"]] = 0
            self.data[self.index_dict["lat_min"]] = 0
            self.data[self.index_dict["long_deg"]] = 0
            self.data[self.index_dict["long_min"]] = 0
        else:
            self.data[self.index_dict["lat_deg"]] = self.read_raw_data(gps.latitude_degrees)
            self.data[self.index_dict["lat_min"]] = self.read_raw_data(self.latitude_minutes)
            self.data[self.index_dict["long_deg"]] = self.read_raw_data(self.longitude_degrees)
            self.data[self.index_dict["long_min"]] = self.read_raw_data(self.longitude_minutes)
        

if __name__ == "__main__":
    gps = GPSDriver()
    gps.update()
    print("Time: " + time.monotonic())
    print("GPS data " + gps.data[1])

    while True:
        # Make sure to call gps.update() every loop iteration and at least twice
        # as fast as data comes from the GPS unit (usually every second).
        # This returns a bool that's true if it parsed new data (you can ignore it
        # though if you don't care and instead look at the has_fix property).
        gps.update()
        # Every second print out current location details if there's a fix.
        current = time.monotonic()
        if current - last_print >= 1.0:
            last_print = current
            if not gps.has_fix:
                # Try again if we don't have a fix yet.
                print("Waiting for fix...")
                continue
            # We have a fix! (gps.has_fix is true)
            # Print out details about the fix like location, date, etc.
            print("=" * 40)  # Print a separator line.
            print(
                "Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(
                    gps.timestamp_utc.tm_mon,  # Grab parts of the time from the
                    gps.timestamp_utc.tm_mday,  # struct_time object that holds
                    gps.timestamp_utc.tm_year,  # the fix time.  Note you might
                    gps.timestamp_utc.tm_hour,  # not get all data like year, day,
                    gps.timestamp_utc.tm_min,  # month!
                    gps.timestamp_utc.tm_sec,
                )
            )
            print("Latitude: {0:.6f} degrees".format(gps.latitude))
            print("Longitude: {0:.6f} degrees".format(gps.longitude))
            print(
                "Precise Latitude: {:2.}{:2.4f} degrees".format(
                    gps.latitude_degrees, gps.latitude_minutes
                )
            )
            print(
                "Precise Longitude: {:2.}{:2.4f} degrees".format(
                    gps.longitude_degrees, gps.longitude_minutes
                )
            )
            print("Fix quality: {}".format(gps.fix_quality))
            # Some attributes beyond latitude, longitude and timestamp are optional
            # and might not be present.  Check if they're None before trying to use!
            if gps.satellites is not None:
                print("# satellites: {}".format(gps.satellites))
            if gps.altitude_m is not None:
                print("Altitude: {} meters".format(gps.altitude_m))
            if gps.speed_knots is not None:
                print("Speed: {} knots".format(gps.speed_knots))
            if gps.track_angle_deg is not None:
                print("Track angle: {} degrees".format(gps.track_angle_deg))
            if gps.horizontal_dilution is not None:
                print("Horizontal dilution: {}".format(gps.horizontal_dilution))
            if gps.height_geoid is not None:
                print("Height geoid: {} meters".format(gps.height_geoid))
    
