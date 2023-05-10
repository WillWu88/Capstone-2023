#ros2 #programming #control 

This [[ROS2]] node deals with the sensor fusions for the position estimations. Check [[Kalman Filter]] for the theory and [[Alpha-Beta-Gamma Filter]].

Important aspects include:
- Class constructor:
```python
 super().__init__('kalman_filter_x')
```
- The node has one publisher objects: `XFiltered` which are the x and y position estimators of the car. 
```python
self.state_pub = self.create_publisher(XFiltered, 'x_filtered', 10)
```
- The node is subscribed to 4 different topics: `gps_raw`, `imu_raw`, `gps_raw` which are the sensor readings and `heading` from the [[Navigation Design]] which indicates whether or not to perform a frame transformation. Note: the sensor subscription publish at different frequencies. The IMU node at a 100Hz, GPS at 10Hz and RPM at 100Hz. We need to synchronize the readings in order to perform estimations.
```python
self.heading_sub = self.create_subscription(Heading, 'heading', self.heading_update, 10)

# time synchronizer for simultaneous sensor reading
self.imu_sub = Subscriber(self, Imu, "/imu_raw", qos_profile = 10)
self.rpm_sub = Subscriber(self, RPM, "/rpm_raw", qos_profile = 10)
self.gps_sub = Subscriber(self, GPS, "/gps_raw", qos_profile = 10)
```
- Approximate time synchronizers are used in order to implement sensor fusions. 
```python
self.time_sync = ApproximateTimeSynchronizer([self.imu_sub, self.rpm_sub],
                                                     10,
                                                     0.01)
self.gps_fusion = ApproximateTimeSynchronizer([self.imu_sub, self.gps_sub],
                                                      10,
                                                      0.01)
```
- GPS and IMU fusion 
- IMU and RPM fusion
- Using the LQR to estimate the full state vector, the constants we used are:
```python
# TUNING SECTION:

# local fast x-axis kf
Q_mult_local_x = 1.
local_ms_mult = 1.5

# global x-axis kf
Q_mult_x = 0.01
R_mult_x = 1000.

# global yaw kf
Q_mult_yaw = 0.1
R_mult_yaw = 1.0
```

