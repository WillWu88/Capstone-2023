[Matlab Learning Extended Kalman Filter Link](https://www.mathworks.com/matlabcentral/fileexchange/18189-learning-the-extended-kalman-filter)

[Matlab Extended Kalman Filter Feature](https://www.mathworks.com/help/ident/ref/extendedkalmanfilter.extendedkalmanfilter.html)

## Basics on Extended Kalman Filter
[Wiki for Extended Kalman Filter](https://en.wikipedia.org/wiki/Extended_Kalman_filter)

- The extended Kalman Filter is the nonlinear version of the Kalman filter which linearizes about an estimate of the current mean and covarience.

- In the extended Kalman filter, the state transition and observation models don't need to be linear functions of the state but may instead be differentiable functions.
	- The function f can be used to compute the predicted state from the previous estimate and similarly the function h can be used to compute the predicted measurement from the predicted state.
	- However, f and h cannot be applied to the covariance directly, instead a matrix of partial derivatives is computed.

- Disadvantages
	- The extended Kalman filter in general is not an optimal estimator.
	- If the initial estimate of the state is wrong, or if the process is modeled incorrectly, the filter may quicly diverge, owing to its linearization.
	- The estimated covariance matric tends to underestimate the true covariance matric nd the risks becoming inconsistent without the addition of "stabilising noise"

- This being said this is still the de facto standard in navigation systems and GPS

- Also has notes on Unscented Kalman Filters. 