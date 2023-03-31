#programming #ros2 #acc #sensor 

A [[ROS2]] node that publishes both raw and filtered RPM sensor readings

## I. Driver Design

### 1. Action Server

The ROS node is implemented as an action server. We chose this implementation for the following reasons:
- The action server follows an asynchronous communication model. The service sends a request, and the server processes the request and sends responses. 
- Two server offers two types of response: feedback and result. We can design the feedback to be instantaneous while the server processes responses. 
- This asynchronous nature is perfect for our RPM sampling process, which needs to execute the timing process before returning a reading

Because the RPM object uses a circular buffer to filter results, we can return the moving average and the latest result stored in the buffer instanteously as the "feedback". When the server finishes, it returns the updated data. 

Though this model works in theory, it also significant drawbacks. Unlike the IMU, this data is not instanteous. Though the feedback is instantaneous, it is an older version of the reading. The server does not start sampling unless the client tells it to. If we integrate the client into a mision-critical node such as the controller, the node will suffer from significant lag and inaccruate reading.


### 2. Alternative: micro-controller co-pilot

- Setting up a [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) as a small [[I2C]] peripheral
- Using the C sdk for Pi Pico, we first migrated the polling calculation onto Pico
	- Circular buffer now keep tracks of time in microseconds instead of recording speed
- The pico is then configured as an I<sup>2</sup>C peripheral with buffer memory. The driver code on Raspberry PI will then read the buffer memory through I<sup>2</sup>C to get the latest reading.

See [[RPM I2C Peripheral]] for detailed implementation.

## II. Publisher node design

###  1. Creating custom srv files

Topics act as a bus for nodes to exchange messages. The structure of each topic is defined by a .srv or .msg file. Unlike the IMU publisher, the encoder does not have a predefined interface definition from existing ROS2 documentation. So, we created a custom .msg file in its own package. 

RPM.msg structure:
```python
std_msgs/Header header
float64 rpmraw
float64 rpmfiltered
```

### 2. Publisher

Important aspects include:
- Importing the built-in message type, which structures the data that passes on the topic.
```python
from tutorial_interfaces.msg import Rpmmsg
```
- Calling the class's constructor and give the node a name:
```python
super().__init__('rpm_publisher')
```
- Creating a publisher object which is in charge of creating the topic and publishing the messages. We used the public method of `rclcpp:Node`: `create_publisher` which returns the `rclcpp:: Publisher` object. 
- Creating a `timer_callback` which increments the message field and call the publisher method at a frequency of 200Hz (so every 0.005s) to publish the message. The message is then published to the console with `get_logger().info` method.
- Creating a `populate_message` function which assigns data to the `header`, `rpmraw` and `rpmfiltered` data types.
- Defining the main function which initializes the rclpy library and "spins" the node using the `rclpy.spin` method to call the callbacks.

## Appendix: References

- [rclpy reference](https://docs.ros2.org/foxy/api/rclpy/index.html)
- [[Python Notes]]
- [Bool Message Type](https://github.com/ros2/common_interfaces/blob/rolling/std_msgs/msg/Bool.msg)
- 