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

