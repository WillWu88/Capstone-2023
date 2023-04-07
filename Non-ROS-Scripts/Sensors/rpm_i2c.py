import smbus

DEV_ADDR = 0x17
I2C_BAUDRATE = 100000

bus = smbus.SMBus(1)

# read first byte
try: 
    sample = bus.read_byte_data(DEV_ADDR, 0x00)
    print(sample)
except OSError:
    print("Wires not connected!")
