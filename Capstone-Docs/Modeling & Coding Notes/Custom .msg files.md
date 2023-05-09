#ros2 #programming 

In a separate package, we created custom .msg files for our topics.

## I. GPS

The GPS node publishes the latitude and longitude positions of the car. These are given in degrees and minutes units. 
```python
std_msgs/Header header
float64 latdeg
float64 longdeg
float64 latmin
float64 longmin
bool flag
```
Check [[GPS Node]] for the usage of the .msg file.

## II. Heading

The Navigation node publishes the heading of the car. Which is an indicator of whether the car has finished turning and a frame transformation needs to be performed to change the axes. This will also indicate to the car to keep it straight until the next point.
```python
std_msgs/Header header
float64 heading
```
Check [[Navigation Design]] for the usage of this .msg file.

## III. PIDPOSE

The PID pose controller node publishes the steering angle $\theta$ that will go directly into the servo mixer.
```python
std_msgs/Header header
float64 theta
float64 debug_error # debugging
float64 debug_unsat_out # debugging
bool turning_override
```
Check [[PID controller nodes]] for the usage of the .msg file.

## IV. PIDVEL

The PID velocity controller node publishes the RPM value which will directly command the motor speed.
```python
std_msgs/Header header
float64 tau
float64 debug_error # debugging
float64 debug_unsat_out # debugging
```
Check [[PID controller nodes]] for the usage of the .msg file.

## V. PoseSetpoint

This custom message publishes the steering angle setpoint by the Navigation node.
```python
std_msgs/Header header
float64 yawsetpoint
float64 macro_heading
bool turning_override
float64 debug_current_heading
float64 debug_target_heading
```
Check [[Navigation Design]] for implementation.

## VI. XFiltered


## References:
- [Tutorial on how to create a custom .msg file](https://docs.ros.org/en/crystal/Tutorials/Custom-ROS2-Interfaces.html#prerequisites)