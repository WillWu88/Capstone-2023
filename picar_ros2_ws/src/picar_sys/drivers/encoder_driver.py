#Reading of 0 means magnet detected,
#reading of 1 means no magnet detected

import RPi.GPIO as IO
import time
import sys
import busio
import math
import numpy as np;
from scipy.io import savemat
from datetime import date

class EncoderDriver():

	def __init__(self, size):
		self.size = size
		self.circ = [0] * self.size
		# zero out initial buffer, fixed sized
		self.write_ptr = 0

        # ---------------------------
        self.index_dict = {
		"raw_rpm": 0,
		"filtered_rpm": 1,
		"commanded_rpm": 2 #commanded will always be 20% for now
        }
        self.data = [0] * len(self.index_dict)
        # ---------------------------


	def updateBuffer(self, new_val):
		self.circ[self.write_ptr % self.size] = new_val #insert new val based on ptr
		self.write_ptr += 1

	def CalcRaw(self, start_time, stop_time):
		raw_rpm = 20/(stop_time - start_time)
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
default_rpm_com = 0.2

if __name__ == "__main__":
	# log user-specified amount of sensor data
	sample_num = int(input(" Input # of data here: >>> "))
    encoder = EncoderDriver()

	if (not(sample_num)):
		while True:
			curr_pin_val = IO.input(GPIO_num) # read rpm value when sensor triggers
			if not(curr_pin_val) and last_val:
				stop = time.perf_counter();
				rpm_filter.CalcRaw(start,stop)
				#print("Filtered: " + str(rpm_filter.CalcFilter()) + "\n")
				last_val = curr_pin_val
				start = stop
			else:
				last_val = curr_pin_val
	else:

		log_data = np.zeros((3,sample_num))
		log_data[index_dict["commanded_rpm"],:] = np.ones((1, sample_num))*default_rpm_com

		sample_count = 0
		print("Collecting data now...")
		try:
			while sample_count < sample_num:
				curr_pin_val = IO.input(GPIO_num) # read rpm value when sensor triggers
				if not(curr_pin_val) and last_val:
					stop = time.perf_counter();
					log_data[index_dict["raw_rpm"], sample_count] = rpm_filter.CalcRaw(start, stop)
					log_data[index_dict["filtered_rpm"], sample_count] = rpm_filter.CalcFilter()
					last_val = curr_pin_val
					start = stop
					sample_count += 1
				else:
					last_val = curr_pin_val

			output_data = {"RPM_sample": log_data}
			date_str = date.today() #system time stamp
			#savemat("./Data/RPM_Data_"+date_str.strftime("%b_%d_%Y") +".mat", output_data)
				
		except KeyboardInterrupt:
			output_data = {"RPM_sample": log_data}
			date_str = date.today() #system time stamp
			#savemat("./Data/RPM_Data_"+date_str.strftime("%b_%d_%Y") +".mat", output_data)
