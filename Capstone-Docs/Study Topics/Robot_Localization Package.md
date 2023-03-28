## Research and Implementation Resources

### Source 1: [Github ROS2 Robot Localization Package Tutorial](https://github.com/methylDragon/ros-sensor-fusion-tutorial/blob/master/01%20-%20ROS%20and%20Sensor%20Fusion%20Tutorial.md)

Statement of Purpose: A tutorial for sensor fusion using the robot_localization package, including explanations of pre-requisite concepts.

Sections:
1) Introduction
2) Concepts
	1) ROS Nav Stack Refresher
	2) Map, Odom, and base_link
	3) Kalman Filters and The Motivations for Sensor Fusion
	4) Covariance
3) Practical sensor fusion with robot_localization
	1) Introduction of robot_localization
	2) Roadmap
	3) Preparing your data
	4) Configuring the Kalman Filter Nodes
	5) Best Practices for Sensor Fusion
	6) Some Handy Configuration Parameters
	7) Fusing GPS Data
	8) rosbag
	9) Kalman Filter Tuning

### Source 2: [ROS official "Robot Localization wiki"](http://docs.ros.org/en/melodic/api/robot_localization/html/)

Summary: Robot_localization is a collection of state estimation nodes, namely the ekf_localization_node (extended kalman filter) and ukf_localization_node (unscented kalman filter), each of which is a nonlinear state estimator for robots moving in 3D space. In addition, it provides navsat_transform_node (*see source 4*) which aids in the integration of GPS data.

Sections:
1) Features
2) Other resources

### Source 3: [Sensor Fusion Using Robot Localization Package Tutorial](https://automaticaddison.com/sensor-fusion-using-the-robot-localization-package-ros-2/)

Summary: A tutorial showing how to set up the robot_localization package in ROS 2, and then gives an example of fusing odometry data with IMU data to correct for wheel slip.

Sections:
1) About the Robot Localization Package
2) Install the Robot Localization Package
3) Set the Configuration Parameters
4) Create a Launch File
5) Build the Package
6) Launch the Robot

### Source 4: [ROS official "navat_transform_node" documentation](http://docs.ros.org/en/melodic/api/robot_localization/html/navsat_transform_node.html)

Summary: Takes in an input of nav_msgs/Odometry (which is usually the output of ekf/ukf_localization_node), a sensor_msgs/Imu containing an accurate estimate of your robots heading, and a sensor_msgs/NavSatFix message containing GPS data. It returns an output odometry message in coordinates that are consistent with your robots world frame.

Sections:
1) Parameters
	1) frequency
	2) delay
	3) magnetic_declination_radians
	4) yaw_offset
	5) zero_altitude
	6) publish_filtered_gps
	7) broadcast_utm_transform
	8) use_odometry_yaw
	9) wait_for_datum
	10) broadcast_utm_transform_as_parent_frame
	11) transform_timeout
2) Subsribed Topics
	1) imu/data
	2) odometry/filtered
	3) gps/fix
3) Published Topics
	1) odometry/gps
	2) gps/filtered
4) Published Transforms
	1) world_frame->utm