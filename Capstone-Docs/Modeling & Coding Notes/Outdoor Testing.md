In preparations for ESE Day we began running our PiCar outdoors, these tests allowed us to gather sensor data to later be used in a Kalman Filter, see the current issues with the Picar's running ability, and test our current scripts for running the PiCar.

## I. Preliminary testing

#### a. IMU 
Gathering IMU data in order to calculate the covariance and the mean of the data, which we will use in the estimation. We find that both of the gyroscopes and accelerations follow a normal distribution. Results:
![IMU acceleration Prefliminary results](Figures/IMU-Reading-acc.png)
![IMU acceleration Prefliminary results](Figures/IMU-Reading-gyro.png)

## b. RPM
Gathering preliminary encoder data to test the accuracy of using a moving average to filter the RPM. Results:

![Prelim RPM data](Figures/rpm_sensor.jpg)

## c. GPS
Testing of GPS sensor. We have the GPS indicate the longitude and latitude in degrees and minutes, which we verified later. The GPS has a very precise and accurate reading of our position.
![GPS Preliminary test](Figures/GPS_set_points/origin-gps.png)

### d. Servo

From our outdoor test we also learned that our servo angle of 0 wasn't actually straight ahead, and that a servo angle of 3 is in fact much closer to straight ahead. The outdoor test also allowed us alot of insight into the speed the car should be running around the track, both on the straight aways and when turning, and gave a clear indication that a PID controller to keep the car from veering off is essential for our final product. 

## II. ROS2 nodes testing