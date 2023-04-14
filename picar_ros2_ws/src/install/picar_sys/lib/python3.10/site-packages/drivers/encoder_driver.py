#Reading of 0 means magnet detected,
#reading of 1 means no magnet detected

import RPi.GPIO as IO
import serial

class EncoderDriver():

    def __init__(self, size):
        self.size = size
        self.circ = [0] * self.size
        # zero out initial buffer, fixed sized
        self.write_ptr = 0
        IO.setwarnings(False)
        IO.setmode(IO.BCM)
        self.GPIO_num = 16
        IO.setup(self.GPIO_num,IO.IN,IO.PUD_UP)
        self.last_val = IO.input(self.GPIO_num)
        self.latest = 0
        self.rpm_filter = 5

    def updateBuffer(self,new_val):
        self.circ[self.write_ptr % self.size] = new_val #insert new val based on ptr
        self.latest = new_val
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
    
    def update(self):
        trig_state = 0
        while True:
            curr_pin_val = IO.input(self.GPIO_num) # read rpm value when sensor triggers
            if not(curr_pin_val) and self.last_val:
                if not(trig_state):
                    start = time.perf_counter()
                    trig_state = trig_state + 1
                else:
                    stop = time.perf_counter()
                    self.CalcRaw(start,stop)
                    self.last_val = curr_pin_val
                    break;
            else:
                self.last_val = curr_pin_val


