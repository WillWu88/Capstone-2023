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

- System dynamics are of second order if the storage of mass 
