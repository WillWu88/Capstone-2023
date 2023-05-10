#theory #sensor

## I. I<sup>2</sup>C Basics

- I<sup>2</sup>C is a serial communication bus protocol
- Supports multi-master, multi-slave
- Two wires:
	- `SDA`: Serial Data
	- `SCL` Serial Clock
	- Both wires are pulled up
- Data synchronized by clock
	- clock signal controlled by master
- Typical I<sup>2</sup>C message is set up as follows
![I2C Message](https://www.circuitbasics.com/wp-content/uploads/2016/01/Introduction-to-I2C-Message-Frame-and-Bit-2-1024x258.png)
- Address frame: slave address

I<sup>2</sup>C communication follows a specific format. The master sends a start signal which acts as a message delimiter and indeicates the beginning of a transmission. The master then sends a 7-bit address slave device it wants to communicate with, followed by a read/write bit that specifies whether the master wants to read from or write to the slave. The slave confirms reception of the address by sending and ACK bit back to the master. Finally, the protocol ends when the master sens a stop signal.

### Setup
[[Sensor SetUp]]

### I2C on Ubuntu:

```shell
# detect i2c address matrix
sudo i2cdetect -y 1
```


## II. SPI



## III. CAN




## Appendix: References
- [Wikipedia Page for I2C ](https://en.wikipedia.org/wiki/I%C2%B2C)