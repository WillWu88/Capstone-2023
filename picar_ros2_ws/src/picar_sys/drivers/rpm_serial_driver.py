import serial

class EncoderDriver():
    
    def __init__(self):
        self.port = serial.Serial('/dev/ttyACM0', baudrate=115200)
        self.backup = 0

    def update(self):
        val = self.port.readline()
        try:
            self.backup = float(val.decode('utf-8').replace('\r\n', ''))
            return self.backup
        except ValueError:
            return self.backup
