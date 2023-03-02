## Deeper dive into Kalman Filter

- [Kalman FIlter wiki](https://en.wikipedia.org/wiki/Kalman_filter)

- Kalman filtering is an algorithm that uses a series of measurements observed over time, including statistical noise and other inaccuracies, and produced estimates of unknown variables that tend to be more accurate than those based on single measurement alone.
	- This is due to estimating a joint probability distribution over the variables for each timeframe.

- The algorithm works by a two-phase process.
	1) The prediction phase: where the Kalman filter produces estimates of the current state variables, along with their uncertainties
	2) The observation of the next measurement: where the previous estimates are updated using a weighted average, with more weight being given to estimates with greater certainty.
	- This algorithm is recursive and operates in real time, using only the present input measurements and the state calculated previously and its uncertainty matrix, no other information is required.

- Optimality of Kalman filtering assumed that errors have a normal distribution.

### Overview of the calculation

- Kalman filtering uses a system's dynamic model, known from the control inputs to that system, and multiple sequential measurements (such as from sensors) to form an estimate of the systems varying quantaties that is better than the estimate obtained by using only one measurement along.

- There are limitors to how well it is possible to determine the system's state:
	- Noisy sensor data
	- Approximations in the equations that describe the system evolution
	- External factors that are not accounted for
- The Kalman filter deals effectively with the uncertainty due to noisy sensor data and, to some extent, with random external factors.

- The Kalman filter produces an estimate of the state of the system as an averafe of the system's predicted state and of the new measurement using a weighted average.
	- The purposed of the weights is that values with better estimated uncertainty are "trusted" more.
	- The weights are calculated from the covariance, a measure of the estimated uncertainty of the prediction of the system's state.
	- The result of the weighted average is a new state estimate that lies between the predicted and measured state, and has better estimated uncertainty than either alone. 
	- This process is repeated recursively, with the new estimate and its covariance informing the prediction used in the following iteration, and requires only the last "best guess", rather than the entire history, of a system's state to calculate a new state. 

	- The Kalman filters gain, or Kalman-gain is the weight given to the measurements and current-state estimate, and can be "tuned" to achieve a particular performance.
		- With a higher gain, the filter places more weight on the most recent measurements, and thus conforms to them more responsively.
		- With a low gain, the filter conforms to the model predictions more closely.
		- At the extremes, a high gain close to one will result in a more jumpy estimated trajectory, while a low gain close to zero will smooth out noise but decreases responsiveness.

- When performing the actual calculations for the filter, the state estimate and covariances are coded into matricies because of the multiple dimensions involved in a single set of calculations. 
	- This allows for a representation of linear relationships between different state variables in any of the transition models or covariances.
