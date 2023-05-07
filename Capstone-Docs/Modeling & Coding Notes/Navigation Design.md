#navigation 

Refer to [[SLAM]] for theory base. The navigation node indicates the heading, the position and velocity setpoints of the car. 

## I. GPS setpoints

During one of our [[Outdoor Testing]]s, we collected GPS points which will determine the turning points of our car. The following map shows the quad on which we will be performing our demonstration. It is located at the south of Brauer Hall, on WashU campus.
![GPS setpoints](Figures/GPS-setpoints.jpeg)

Legend:
- Blue point is the origin, we set this to be point (0,0) in cartesian.
- Red points are the turning points. At these points, the car to go slower and to set the wheels at a turning angle.
- Pink points are when the car changes heading, within the ROS code a frame transformation happens as we are changing the body frame's orientation. The x and y axis are oriented differently after each turn. Additionally, the car's steering angle is adjusted so that the car can keep straight.

## II. Navigation node

The navigation node is subscribed to the position estimator. 