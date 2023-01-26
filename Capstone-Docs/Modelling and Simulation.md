## I. Background

Refer to [[Dynamic Systems]] and [[System Modeling]] for modelling technique

Inputs of the system:
- Steering angle (delta)
- Longitudinal slip from the front wheels
- Torque from the motor acting on back wheels

## II. Statespace Model of PiCar

We define the state vector of the car as follows:

$$\vec{x} = \begin{bmatrix}\dot{x} \\ \dot{y} \\ \dot{\psi}\end{bmatrix} = \begin{bmatrix}v_x \\ v_y \\ r_z\end{bmatrix}$$
where $x$ and $y$ are the displacement of the car from an arbitrary starting point. We might extend our model to include these displacement states if we can aquire localization information, i.e global/local position through GPS or SLAM. $v_x$ and $v_y$ denote the translational speed of the car along their respective axis,  while $\psi$ and $r_z$ denotes angular quantities (right-hand rotation around a downward z-axis), yawing angle and yawing velocity to be exact. 

Our dynamic system contains two inputs: steering angle $\theta$ and motor torque $\tau_m$. Though we can control $\theta$ with direct command from the Raspberry Pi, we indirectly control $\tau_m$ by varying the voltage. See [[System Identification]] and [[#III. Actuator Modelling]] for details.

We build our model based on two fundamental principles of physics: Newton's Sec ond Law, and Conservation of Net Torque.

$$F = ma,\; \tau = I\alpha$$

## III. Actuator Modelling


## Appendix: References
- [Matlab Vehicle Modelling](https://www.mathworks.com/help/ident/ug/modeling-a-vehicle-dynamics-system.html)
