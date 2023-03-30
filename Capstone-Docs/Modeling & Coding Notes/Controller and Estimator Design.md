#design

Controller 

refer to [[Estimators]] and [[Feedback Loops]] for theoretical background

## I. Kalman Filter Design

There are three pieces to the "puzzle" of implementing a rudimentary Kalman filter. 
1. Discretized dynamics model describing the dynamics of the applied input and the states of interest
2. Process input, coming from the sensor
3. Noise distribution of the sensor, collected at 0 bias.

We are mainly interested in designing three kalman filters, measuring our three interested state variables, as outlined by [[PiCar Modelling and Simulation]]
$$\vec{x} = \begin{bmatrix}v_x \\ v_y \\ r_z\end{bmatrix}$$

### 1. Y-Axis Kalman Filter Design




## Appendix: References

### IMU Filter Notes
- [Comparison of complementary and Kalman filters for IMU](https://aip.scitation.org/doi/pdf/10.1063/1.5018520#:~:text=Since%20Kalman%20filter%20is%20a,the%20statistically%20most%20optimal%20value.)

