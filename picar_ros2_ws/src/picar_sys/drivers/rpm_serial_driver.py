import serial

class EncoderDriver():
    
    def __init__(self):
        self.port = serial.Serial('/dev/ttyACM0', baudrate=115200)
        self.backup = 0

    def update(self):
        val = self.port.readline()
        try:
            new = float(val.decode('utf-8').replace('\r\n', ''))
        except ValueError:
            return self.backup
        else:
            # eliminate data spikes
            if (new >= 3000):
                return self.backup
            else:
                self.backup = new
                return self.backup

