### 10.1 Basic Control Functions

- Most PID controllers do not use derivative action, but PID is the generic term for this class of controller.

- PID controllers are often shown with block diagrams:
	- $u$ is the control signal for the sustem
	- $e$ is the error 
	- $k_r$ is the feedforward term
	- $r$ the command or reference signal aka setpoint.
	- $k_p$ the proportional gain
	- $k_i$ the integral gain
	- $k_d$ the derivative gain
	- $u_{ff}$ feedforward term adjusted for steady state, or reset.

- The control action is the sum of three terms: proportional feedback, the integral term and derivative action.

- Start by considering pure proportional feedback, and adjusting the proportional term to avoid steady-state error.

- Integral action guarentees that the process output agrees with the reference in steady state and provides an alternative to the feedforward term.

- Using integral action to achieve zero steady-state error is much better than using feedforward, which requires a precise knowledge of process parameters.

- Integral action can also be viewed as a method for generating the feedforward term $u_{ff}$ in the proportional controller automatically.
	- One way to do this is where the controller output is low-pass-filtered and fed back with positive gain.
	- This is called automatic reset

- The integral gain $k_i$ is a useful measure for attenuation of load disturbances.

- The intrgrated error is thus inversely proportional to the integral gain.

- A large gain $k_i$ attenuates disturbances effectively, but too large a gain gives oscillatory behavior, poor robustness and possibly instability.

- The original motivation for derivative feedback was to provide predictive or anticipatory action.

- Derivative action can be implemented by taking the difference between the signal and its low-pass filtered version.

- The system is oscillatory when no derivative action is used, and it becomes more damped as the derivative gain is increased. Performance deteriorates if the derivative gain is too high.

### 10.2 Simple Controllers for Complex Systems

- Low-order models can be obtained from first principles. 
	- Any system can be modeled by a static system if its inputs are sufficiently slow. 
	- A first-order model is sufficient if the storage of mass, momnetum or energy can be captured by only one variable.

- System dynamics are of second order if the storage of mass, energy and momentum can be captured by two state variables.

- A wide range of techniques for model reduction are also available.

- We begin by analyzing the case of integral control.
	- A stable system can be controlled by an integral controller provided that the requirements on the closed loop system are modest.
	- To design the controller we assume that the transfer function of the process is a constant.
	- The loop transfer function under integral control then becomes $K*k_{i}/s$, and then the closed loop charactreistic polynomial is simply $s + K*k_{i}$
	- Analysis requires that $T_{cl}$ br sufficiently large that the process transfer function can be approimated by a constant.

- Book example, see page 311 of the text, *Integral control of AFM in tapping mode*

- Book example, see page 312 of the text, *Cruise control using PI feedback*
	- Considers the problem of maintaining the speed of a car as it goes up a hill.

- A PI controller can also be used for a process with second-order dynamics, but there will be restrictions on the possible locations of the closed loop poles.
	- Using a PID controller, it is possible to control a system of second order in such a way that the closed loop poles have arbitrary locations.

### 10.3 PID Tuning

- Users of control systems are frequently faced with the task of adjusting the controller parameters to obtain a desired  behavior. 
	- Since the PID controller has so few parameters, a number of special empirical methods have also been developed for direct adjustmet of the controller parameters.

#### Ziegler-Nichols' Tuning

- In the 1940s, two methods for controller tuning based on simple characterization of process dynamics in the time and frequency domains.
	- The time domain method is based on a measurement of a part of the open loop unit step response of the process. A controller was tuned manually for each process, and an attempt was then made to correlate the controller parameters with *a and tau*
	- In the frequency domain method, a controller is connected to the process, the integral and derivative gains are set to zero and proportional gain is increased until the system starts to oscillate.

- The Ziegler-Nichols tuning rules unfortunately have two severe drawbacks: too little process information is used, and the closed loop system that are obtained lack robustness. 

- Book example on page 316, *Atomic force microscope in tapping mode*

#### Relay Feedback

- The Ziegler-Nichols frequency response method increases the gain of a proportional controller until oscillation to determine the critical gain $k_{c}$ and the corresponding critical period $T_{c}$ or, equivalently, the point where the Nyquist curve intersects the negative real axis.

- The critical period is simply the period of the oscillation. To determine the critical gain we expand the square wave relay output in a Fourier series.

- $K_{c} = (4d)/(a*pi)$
- Having obtained the critical gain $K_{c}$ and the critical period $T_{c}$ the controller parameters can then be determined using the Ziegler-Nichols rules.

- Automatic tuning based on relay feedback is used in many commercial PID controllers. Tuning is accomplished simply by pushing a button that activates relay feedback.

### 10.4 Integrator Windup

- Many aspects of a control system can be understoof from linear models, however there are some nonlinear phenomena that must be taken into account.
	- There are typically limitations in the actuators.

- For a system that operates over a wide range of conditions, it may happen that the control variables reaches the actuator limits, this causes the feedback loop to be broken and the system runs in open loopbecause the actuator remains at its limit independently of the process output as long as the actuator remains saturated.
- The intrgral term and controller output may then become very large, this causes large transcients.

- Book example on page 318 *10.5 Cruise control*
	- Illustrates what happens when a car encounters a hill that is so steep that the throttle saturates when the cruise controller attempts to maintain speed.
	- There are several methods to avoid windup.

- Book examples on page 319 *10.6 Cruise control with anti-windup*
	- Shows the results of controller anti-windup being implimented.

### 10.5 Implementation

- Many practical issues that have to be considered when implementing PID controllers.

#### Filtering the Derivative

- A drawback with derivative action is that an ideal dericative has high gain for high-frequency signals.

- This means that high-frequency measurement noise will generate large variations in the control signal.

- Filtering is obtained automatically if the derivative is implemented by taking the difference between the signal and its filtered version.

- Instead of filtering just the derivative, it is also possibe to use an ideal controller and filter the measured signal.

#### Setpoint Weighting 

- Integral action has to act on the error to make sure that the error goes to zero in steady state.

- The response to reference signals is different because it depends on the values of beta and gamma, which are called reference weights or setpoint weights.

- Book problem on page 321, *Cruise control with setpoint weighting*
	- Shows the effect of setpoint weighting on the response of the system to a reference signal.

#### Implementation Based on Operational Amplifiers

- PID controllers have been implemented in different technologies.

- A PID controller we will use the approximate relation between the input voltage *e* and the output voltage *u* of te op amp.

#### Computer Implementation

- This section describes how a PID controller may be implemented using a computer.
	- The sequence of operation is as follows:
	1) Wait for clock interrupt
	2) Read input from sensor
	3) Compute control signal
	4) Send output to the actuator
	5) Update controller variables
	6) Repeat

- To implement the system using a computer, the continuous-time system has to be approimated by a discrete time system. 

- PID Controller psuedocode on page 324.




