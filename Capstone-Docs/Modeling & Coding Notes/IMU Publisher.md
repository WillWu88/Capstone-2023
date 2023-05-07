#programming #ros2 #acc #sensor 

A [[ROS2]] node that publishes raw IMU readings

## I. IMU driver -- will need explanation of the conversion!!!

To see the sensor configuration and setups refer to [[MPU6050 Configuration]].

The accelerometer and gyroscope values are 16-bit, and are stored in the following array:
```python
self.index_dict = {

            "acc_x": 0,
            "acc_y": 1,
            "acc_z": 2,

            "gyro_x": 3,
            "gyro_y": 4,
            "gyro_z": 5
        }
```

To convert them to actual metric units, we concatenate the high and low bit values, and convert them accordingly.

```python
#Read Accelerometer and Gyro value, then convert

self.data[self.index_dict["acc_x"]] = self.read_raw_data(ACCEL_XOUT_H)/16384.0

self.data[self.index_dict["acc_y"]] = self.read_raw_data(ACCEL_YOUT_H)/16384.0

self.data[self.index_dict["acc_z"]] = self.read_raw_data(ACCEL_ZOUT_H)/16384.0  

#Read Gyroscope raw value

self.data[self.index_dict["gyro_x"]] = self.read_raw_data(GYRO_XOUT_H)/131.0

self.data[self.index_dict["gyro_y"]] = self.read_raw_data(GYRO_YOUT_H)/131.0

self.data[self.index_dict["gyro_z"]] = self.read_raw_data(GYRO_ZOUT_H)/131.0
```

## II. Node Design

Important aspects include:
- Using datatype: `IMU` from `sensor_msgs`
	- Refer to "geometry_msgs" [[#Appendix: References]] 
- Calling the class's constructor and give the node a name:
```python
super().__init__('imu_publisher')
```
- Creating a publisher object which is in charge of creating the topic and publishing the messages. We used the public method of `rclcpp:Node`: `create_publisher` which returns the `rclcpp:: Publisher` object. 
- Creating a `timer_callback` which increments the message field and call the publisher method at a frequency of 100Hz (so every 0.01s) to publish the message. The message is then published to the console with `get_logger().info` method.
- Creating a `populate_message` function which assigns the sensor readings to the datatype.
- Defining the main function which initializes the rclpy library and "spins" the node using the `rclpy.spin` method to call the callbacks.

## Appendix: References

- [ROS Index: Geometry_msgs](https://index.ros.org/p/geometry_msgs/github-ros2-common_interfaces/#humble)
- [rclpy reference](https://docs.ros2.org/foxy/api/rclpy/index.html)
- [[Python Notes]]
- [ROS 2 Documentation: How to write a publisher node] (https://docs.ros.org/en/galactic/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)
