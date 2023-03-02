#theory 


## I. Kalman Filter

Kalman filter recursively receives noisy measurements, and predicts the correct system state based on the noise-distribution of the measurements and internal model of the dynamics. 

### 1. Mathematical Background

Kalman filter is a linear-quadratic estimator (observer). It can be roughly described as an internal discrete-time process model that attempts to produce measurement $\hat{x}$ where $\| \vec{\hat{x}} - \vec{x} \|^2$ converges to zero quickly.

A kalman filter model can be described as follows:
$$x_{k+1} = \hat{A_k}x_k + \hat{B_k}u_k + w_k$$

Where $x_k$ is the discrete-time Kalman filter state, $u_k$ is the process model input, and $w_k$ is the process noise, which roughly follows a gaussian distribution:
$$w_k \sim \mathcal{N}(0,Q_k)$$

where $Q_k$ is the covariance matrix of the distribution.

The model can also receive observations $z_k$ made of the true state $x_k$, where
$$z_k = H_k x_k + v_k$$
Note that $H_k$ denotes the measurement model and $v_k$ denotes the observation noise, which also follows a gaussian distribution centered around 0 with covariance $R_k$
$$v_k \sim \mathcal{N}(0,R_k)$$
Note that the noise random vectors and the initial condition are assumed to be independent. 

Kalman filter resembles a [[Alpha-Beta-Gamma Filter]]


### 2. Filtering Process

Kalman filtering is a two-step process, consisting of "predict" step and "update" step. 

**Read more:** [[ALS: Autocovariance Least-Sqaures]] for noise covariance measurement


## II. Sensor Fusion

All sensor interface can be found in [[Sensors & Electronics]]


## Appendix: References
- [Kalman Filter Wikipedia](https://en.wikipedia.org/wiki/Kalman_filter)
- [Control Bootcamp Lecture](https://www.youtube.com/watch?v=s_9InuQAx-g)
- ESE-4481 Lecture Notes
	- [[stateEstimationHelp.pdf]]
- [Kalman Filter Tutorial](https://www.kalmanfilter.net/kalman1d.html#page-top)
