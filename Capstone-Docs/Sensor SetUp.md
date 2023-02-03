## 1. I2C Setup Scripts
```shell
sudo apt install raspi-config # pi manager to enable rpi bus protocols
pip3 install smbus #accelerometer package
sudo apt install python3-pigpio #python gpio package for raspberry pi
sudo apt install python3-lgpio
sudo apt install i2c-tools libi2c-dev #i2c package
```

- [I2C Setup](https://askubuntu.com/questions/1273700/enable-spi-and-i2c-on-ubuntu-20-04-raspberry-pi)

Follow [this](https://abyz.me.uk/rpi/pigpio/download.html)  and [this](https://forums.raspberrypi.com/viewtopic.php?t=319761) for *pigpio* setup 
- play around with executables, as ubuntu can be iffy
- Update I2C permission: [Link](https://ask.wingware.com/question/3/i2c-problem-with-remote-raspberry-pi/)

### Lidar Setup Scripts
```shell
sudo pip3 install rplidar-roboticia
```

Utilizing sample code found on Github [Lidar Sample Code Github](https://github.com/Roboticia/RPLidar) we were able to get preliminary data on the Lidar. 

### MPU6050 Setup Scripts
//Will, fill in any inital scripts for getting this to run if there was any

- [[MPU6050 Setup]]

Follow [this](https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf) for the register map of the MPU6050.
- Key registers and their functionalities are listen in the MPU6050 setup.
