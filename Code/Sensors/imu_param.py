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
