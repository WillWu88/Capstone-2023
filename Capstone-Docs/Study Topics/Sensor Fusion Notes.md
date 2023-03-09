## GPS-IMU

### Research Links 

### Link 1: 
[GPS/IMU Data Fusion using Multisensor Kalman Filtering : Introduction of Contextual Aspects](https://www.stats.ox.ac.uk/~caron/Publications/J_Information_Fusion_2004.pdf)

Abstract Summary:
Aim of the acticle is to develop a GPS/IMU Multisensor fusion algorithm. The algorithm was made by fusing GPS and IMU data coming from real tests on a land vehicle. Because the lack of credibility of GPS signal in some cases and because of the drift of the INS, so to avoid this problem authors propose to feed the fusion process based on a multisensor Kalman filter directly with the acceleration provided by the IMU.

Sections:
1) Introduction
2) Multisensor Kalman Filtering
3) Contextual information
4) GPS/IMU data fusion
	1) *Definition of the state and measurement models*
	2) *Definition of the contextual space*
	3) *Equations of the Kalman Filter*
5) Simulation
6) Conclusion and further research

### Link 2:
[Performance of GPS and IMU sensor fusion using unscented Kalman
filter for precise i-Boat navigation in infinite wide waters](https://reader.elsevier.com/reader/sd/pii/S1674984722000969?token=C0355CE6FFFB82545E6C71AC83D91C368A94951A1E60A71AF7B674C4849ABC68E7FB953C814D2521EC9B139E3FDD25E0&originRegion=us-east-1&originCreation=20230306014544)

Abstract Summary: USV navigation, needs to avoid obstacles and carry out automatic movements. One of the siluations is to correct the error of the sensors by GPS/IMU fusion. Using the Unscented Kalman filter sensor fusion, two scenarios were conducted in simulations: results showed position estimate in Scenario II was better.

Sections:
1) Introduction
2) Sensor measurement experiment
	1) Design of GPS and IMU measurement
	2) Filtering method
3) Result and analysis
4) Discussion
5) Conclusions

### Link 3:
[Matlab Mathworks Page: IMU and GPS Fusion for Inertial Navigation](https://www.mathworks.com/help/fusion/ug/imu-and-gps-fusion-for-inertial-navigation.html)

Description Summary:
Example shows how you may build an IMU + GPS Fusion algorithm suitable for UAVs or quadcopters

Sections:
1) Simulation Setup
2) Fusion Filter
3) UAV Trajectory
4) GPS Sensor
5) IMU Sensors
6) Initialize the State Vector of the insfilterMARG
7) Initialize the Variances of the insfilterMARG
8) Initialize Scopes
9) Simulation Loop
10) Error Metric Computation

### Link 4:
[GPS and IMU Sensor Fusion to Improve Velocity Accuracy](http://uu.diva-portal.org/smash/get/diva2:1682155/FULLTEXT01.pdf)

Abstact Summary: Project explores the possibilities on how to improve the accuracy of GPS velocity data by using sensor fusion with an extended Kalman filter. Unscented Kalman filter, particle filter, and neutral network are more difficult than the extended Kalman filter.

Sections:
1) Introduction
	1) Problem description
	2) Background
2) Theory
	1) GPS
	2) IMU
	3) Kalman Filters
	4) Sensor Fusion
3) Methods
	1) Data acquisition
	2) Physical model and general approach
	3) Sensor Fuison of GPS and IMU
	4) [[Extended Kalman Filter]]
4) Results
	1) Quaternion verification
	2) [[Extended Kalman Filter]]
		1) No Delay Compensation
		2) Delay Compensation
		3) Larger Dataset
5) Discussion
	1) Quaternion verification
	2) Sensor fusion with EKF
	3) Further Improvements
	4) Other approaches and implementation
6) Conclusion
7) MATLAB Code

### Link 5:
[Github for: Extended Kalman Filter (GPS, Velocity and IMU fusion)](https://github.com/sugbuv/EKF_IMU_GPS)
[Sensor Fusion GPS+IMU](https://canvas.kth.se/courses/4962/files/805888/download?wrap=1)

Goal Summary: Goal of this algorithm is to enhance the accuracy of GPS reading based on IMU reading. Extended Kalman Filter algorithm shall fuse the GPS reading and Velocities with 9 axis IMU. 

ReadMe Sections:
1) Goal
2) Dependencies
3) How to
	1) Compile
	2) Execute
4) EKF 15 States
	1) Inputs
	2) Outputs
	3) Bias Outputs
5) Result
6) Credits

### Link 6:
[Sensor Fusion: Extended Kalman Filter (EKF)](https://kusemanohar.wordpress.com/2020/04/08/sensor-fusion-extended-kalman-filter-ekf/)

Overview Summary: Extended Kalman Filter, sensor fusion of IMU measurements and estimates from other SLAM algorithm.  Uses Extended Kalman Filter, Camera + IMU (loose fusion)

Sections: 
1) Kalman Filter
2) IMU Process Model
	1) States
	2) Gyroscope Measurements
	3) Accelerometer Measurements
	4) Process Model
3) Linearization
4) Continous ODE to Discrete ODE