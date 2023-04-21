import serial
import numpy as np
from scipy.io import savemat
from datetime import date

encoder = serial.Serial('/dev/ttyACM0', baudrate=115200)

def parseSerial(port, last):
    val = port.readline()
    try:
        return float(val.decode('utf-8').replace('\r\n', ''))
    except ValueError:
        return last

if __name__ == "__main__":
    # log user-specified amount of sensor data
    sample_num = int(input(" Input # of data here: >>> "))
    last = 0.0
    new = 0.0

    if (not(sample_num)):
        while True:
            new = parseSerial(encoder, last)
            print(new)
            last = new

    else:

        log_data = np.zeros((2,sample_num))
        log_data[0,:] = np.ones((1, sample_num))*0.2

        sample_count = 0
        print("Collecting data now...")
        try:
            while sample_count < sample_num:
                new = parseSerial(encoder, last)
                log_data[1, sample_count] = new
                sample_count = sample_count + 1
                last = new

            output_data = {"RPM_sample": log_data}
            date_str = date.today() #system time stamp
            savemat("./Data/RPM_Data_"+date_str.strftime("%b_%d_%Y") +".mat", output_data)
                
        except KeyboardInterrupt:
            output_data = {"RPM_sample": log_data}
            date_str = date.today() #system time stamp
            savemat("./Data/RPM_Data_"+date_str.strftime("%b_%d_%Y") +".mat", output_data)
