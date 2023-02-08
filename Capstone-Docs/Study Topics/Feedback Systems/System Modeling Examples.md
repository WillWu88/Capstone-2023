#theory #control 
## Cruise Control

- Attempts to maintain a constant velocity in the presence of disturbances (primarily the slope of the road).

- To do this, a PI controller is used to receive velocity signals and generates a control signal which is then sent to the actuator, which controls throttle position, which in tern controls the torque delivered by the engine which in turn has an impact on the force that moves the car.

- An FSM can be used to model a controller.