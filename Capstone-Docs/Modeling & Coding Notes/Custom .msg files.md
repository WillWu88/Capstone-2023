#ros2 #programming 

In a separate package, we created custom .msg files for our topics.

## I. GPS

The [[GPS node]] publishes the latitude and longitude positions of the car. These are given in degrees and minutes units. 
```python
std_msgs/Header header
float64 latdeg
float64 longdeg
float64 latmin
float64 longmin
bool flag
```

## II. RPM

The [[RPM Publisher]] publishes the velocity of the car.
```python
std_msgs/Header header
float64 rpmraw
float64 rpmfiltered
float64 derivedms
```

## III. Heading

The Navigation node publishes the heading of the car. Which is an indicator of whether the car has finished turning and a frame transformation needs to be performed to change the axes. This will also indicate to the car to keep it straight until the next point.
```python
std_msgs/Header header
float64 heading
```
Check [[Navigation Design]] for the usage of this .msg file.

## IV. PIDPOSE

The PID pose controller node publishes the steering angle $\theta$ that will go directly into the servo mixer.
```python
std_msgs/Header header
float64 theta
bool turning_override
```
Check [[PID controller nodes]] for the usage of the .msg file.

## V. PIDVEL

The PID velocity controller node publishes the RPM value which will directly command the motor speed.
```python
std_msgs/Header header
float64 tau
```
Check [[PID controller nodes]] for the usage of the .msg file.

## VI. PoseSetpoint

This custom message publishes the steering angle setpoint by the Navigation node.
```python
std_msgs/Header header
float64 yawsetpoint
float64 macro_heading
bool turning_override
```
Check [[Navigation Design]] for implementation.

## VII. VelSetpoint

[[Navigation Design]] publishes the set velocity at each set point.
```python
std_msgs/Header header
float64 target
bool kill_switch
```
The `kill_switch` was for testing purposes, whenever we'd lose control of the car this boolean would shut off the motor. 

## VIII. XFiltered

The [[Kalman Filter node]] publishes the x and y position estimations.
```python
std_msgs/Header header
# earth frame quantities
float64 xpos
float64 xvel
float64 ypos
float64 yvel
float64 yaw
float64 yawvel
# body frame quantities
float64 xbvel
float64 ybvel
# weighted consensus
float64 weighted_x_pos
```

## References:
- [Tutorial on how to create a custom .msg file](https://docs.ros.org/en/crystal/Tutorials/Custom-ROS2-Interfaces.html#prerequisites)