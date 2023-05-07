#sensor #acc #programming 

## I. Preliminary notes:

The IMU utilizes the \_H, highbit, features for accelerometer and gyro values. This allows for easy access to lowbit values by simply interating the address value. The device address utilizes 0x68. 

The entire system runs on the sample rate, which we can set, with a default accelerometer sample rate of 1kHZ and gyroscope sample rate of 8kHz (which can be changed to 1kHz).

## II. Functionality of each register:

#### a. SMPLRT_DIV:

This register generates the Sample rate for the MPU-60X0 from the gyroscope output rate. It uses the following equation: 
*Sample Rate = Gyroscope Output Rate / (1 + SMPLRT_DIV).
Where the Gyroscopic Output Rate is 8kHz when DLPF is disabled (as we intend on using it) and 1kHz when enabled.

#### b. PWR_MGMT_1:

The lower 3 bits are used for CLKSEL, this chooses a clock reference for the system. The spec sheet strongly recommends picking one of the gyroscopes as the reference, CLKSEL 1, 2 & 3.
*google PLL*
- Bit 3 is for TEMP_DIS which is not necessary for our purposes
- Bit5 is for CYCLE, and when this bit is set and SLEEP is disabled, the device cycles between sleep mode and waking up to take a single sample as a rate determined by LP_WAKE_CTRL
- Bit6 is for SLEEP, and when it is set the device enters sleep mode.
- Bit7 is for DEVICE_RESET, and when this bit is set all internal registers return to their default values.

#### c. Config:

- The bottom 3 bits are used to set the DLPF_CFG which corresponds to the accelerometer and gyroscope bandwidth and delay (and frequency for gyroscope).
| DLPF_CFG | Acc B-width (Hz) | Acc Delay (ms) | Gyro B-width (Hz) | Gyro Delay (ms) | Gyro Fs (kHz) |
| ---- | - | - | - | - | - |
| 0 | 260 | 0 | 256 | 0.98 | 8 |
| 1 | 184 | 2.0 | 188 | 1.9 | 1 |
| 2 | 94 | 3.0 | 98 | 2.8 | 1 |
| 3 | 44 | 4.9 | 42 | 4.8 | 1 |
| 4 | 21 | 8.5 | 20 | 8.3 | 1 |
| 5 | 10 | 13.8 | 10 | 13.4 | 1 |
| 6 | 5 | 19.0 | 5 | 18.6 | 1 |
| 7 | reserved | reserved| reserved | reserved | 8 |
- The 3-5 bits are used to set the EXT_SYNC_SET which is currently set to input disabled, otherwise it allows for short strobes to be captured wiht the FSYNC pin.

#### d. GYRO_CONFIG:

- The 3&4 bits correspond to FS_SEL which selects the full scale range of gyroscope outputs.
| FS_SEL | Full Scale Range |
| ---- | - | 
| 0 | +- 250 | 
| 1 | +- 500 | 
| 2 | +- 1000 | 
| 3 | +- 2000 | 
- Bit 5 is the ZG_ST, and setting this bit causes the Z axis gyroscope to perform self test.
- Bit 6 is the YG_ST, and setting this bit causes the Y axis gyroscope to perform self test.
- Bit 7 is the XG_ST, and setting this bit causes the X axis gyroscope to perform self test.

#### e. INT_ENABLE: 

- Bit 0 is DATA_RDY_EN and when set to 1, this bit enables the Data Ready interrupt, which o ccurs each time a write operation to all of the sensor registers has been completed.
- Bits 4&5 also have purpose, however we will not use them in our project.

## III. IMU driver parameter

List of the sensor configurations, setups and MPU6050 register addresses:
```python
#Sensor configuration
INPUT_DISABLED_MAX_FS = 0; #EXT_SYNC_SET 0, DLPF_CFG 0

#Gyro setup
X_SELF_TEST = 128; #perform sensor self test on axis

Y_SELF_TEST = 64;

Z_SELF_TEST = 32;

GYRO_FULL_RANGE = 3 << 3; #+-1000 deg

GYRO_MIN_RANGE = 0 << 3; #+-250 deg

#Sampling Rate

ONE_K_HZ = 7;

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B

SMPLRT_DIV   = 0x19

CONFIG       = 0x1A

GYRO_CONFIG  = 0x1B

INT_ENABLE   = 0x38

ACCEL_XOUT_H = 0x3B

ACCEL_YOUT_H = 0x3D

ACCEL_ZOUT_H = 0x3F

GYRO_XOUT_H  = 0x43

GYRO_YOUT_H  = 0x45

GYRO_ZOUT_H  = 0x47
```

## IV. IMU driver initialization

Once we have the parameters, we can set them to each register accordingly by calling `bus_write_byte_data`. For more explanation refer to [[I2C]].
```python
def MPU_Init(self):
#write to sample rate register
        self.bus.write_byte_data(self.device_address, SMPLRT_DIV, ONE_K_HZ)

        #gyro sampling at 1kHz

        #Write to power management register

        self.bus.write_byte_data(self.device_address, PWR_MGMT_1, 1)

        #Write to Configuration register

        self.bus.write_byte_data(self.device_address, CONFIG, INPUT_DISABLED_MAX_FS)

        #Write to Gyro configuration register

        self.bus.write_byte_data(self.device_address, GYRO_CONFIG, GYRO_MIN_RANGE)

        #Write to interrupt enable register

        self.bus.write_byte_data(self.device_address, INT_ENABLE, 1)
```

## References:
- [MPU6050 documentation](https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf)