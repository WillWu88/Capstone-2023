# Sensor Config Parameters

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
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47
