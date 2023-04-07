import serial

encoder = serial.Serial('/dev/ttyACM0', baudrate=115200)

def parseSerial(port):
    val = port.readline()
    return float(val.decode('utf-8').replace('\r\n', ''))

while True:
    # print(encoder.readline())
    print(parseSerial(encoder))
