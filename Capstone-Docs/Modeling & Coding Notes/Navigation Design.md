#navigation 

Refer to [[SLAM]] for theory base. The navigation node indicates the heading, the position and velocity setpoints of the car. 

## I. GPS setpoints

During one of our [[Outdoor Testing]]s, we collected GPS points which will determine the turning points of our car. The following map shows the quad on which we will be performing our demonstration. It is located at the south of Brauer Hall, on WashU campus.
![GPS setpoints](Figures/GPS-setpoints.jpeg)

Legend:
- Blue point is the origin, we set this to be point (0,0) in cartesian.
- Red points are the turning points. At these points, the car to go slower and to set the wheels at a turning angle.
- Pink points are when the car changes heading, within the ROS code a frame transformation happens as we are changing the body frame's orientation. The x and y axis are oriented differently after each turn. Additionally, the car's steering angle is adjusted so that the car can keep straight.

## II. Methods

The navigation node has all of the points shown in the above map in a queue (see [Python queue](https://docs.ros.org/en/foxy/Tutorials/Intermediate/Writing-an-Action-Server-Client/Py.html)). A queue is a linear data structure which stores data in a First In First Out (FIFO) manner. Once we've arrived within 0.2 meters of the current setpoint, it is popped off the queue so the next setpoint is set as the new target. 

The queues have the longitude and latitude coordinates of each setpoint as well as their status are described as the legend above.

A difficulty of this project are the frame differences. The raw GPS readings are given in the [Earth's reference frame](https://spotlight.unavco.org/how-gps-works/gps-basics/gps-reference-frames.html), while most of the velocity and the position are done in the body frame. When the car makes a turn, the axis of the car is flipped 90° clockwise. We need to take this in account and perform a frame transformation after completing each turn. The heading message from the navigation node indicates when to make this transformation after the pink setpoints indicated above.

## III. Navigation node

The navigation node is an important part of our design as it sets the velocity and angles of our car.

- Class constructor:
```python
super().__init__('navigation_publisher')
```
- The navigation node is subscribed to the [[Kalman Filter node]] and the [[GPS Node]]. The distance between the car and the current setpoint is calculated from the position estimate and the raw GPS readings. 
```python
# Subscribers
self.kf_sub = self.create_subscription(XFiltered, 'x_filtered', self.kf_callback, 10)

self.gps_sub = self.create_subscription(GPS, 'gps_raw', self.gps_callback, 10)
```
- Both subscriptions have their own callback functions `kf_callback` and `gps_callback`. The `gps_callback` function calculates the distance between the origin and the current position (in longitude and latitude) and updates the target. 
  
- The node has three publishers, which are the Heading, angle $\theta$ and the velocity.
```python
self.heading_pub = self.create_publisher(Heading, 'heading', 10)

self.pose_pub = self.create_publisher(PoseSetpoint, 'pose_setpoint', 10)

self.vel_pub = self.create_publisher(VelSetpoint, 'vel_setpoint', 10)
```

- The `car_arrived` function checks if the car's position is within 0.2 meters from the setpoint. If the function returns True the current setpoint and the current turn status gets updated.
```python
def car_arrived(self):

        if (self.curr_x - self.target_x) ** 2 < 0.2:
            return True
        else:
            return False
```

- The `timer_callback` function deals with setting a publishing frequency of 5Hz.
```python
def timer_callback(self):

        # Set point

        msg_setpoint  = self.populate_message('pose_set_point')

        self.pose_pub.publish(msg_setpoint)

        # Vel set point

        msg_velsetpoint = self.populate_message('vel_set_point')

        self.vel_pub.publish(msg_velsetpoint)

        # Heading

        msg_heading = self.populate_message('heading')

        self.heading_pub.publish(msg_heading)
```

- The `populate_message` function sets all the messages accordingly:
```python
def populate_message(self, msg_type):

        match msg_type:

            case 'pose_set_point':

                msg = PoseSetpoint()

                # peek the queue

                if (not (self.stop_now)):

                    msg.xsetpoint = point_q[0][coord_label["lat"]]

                    msg.ysetpoint = point_q[0][coord_label["long"]]

                msg.yawsetpoint = 0. # stay straight

                msg.macro_heading = self.heading

                msg.header.frame_id = 'earth'

                msg.turning_override = self.turn_now

            case 'vel_set_point':

                msg = VelSetpoint()

                msg.target = self.target_vel

                msg.kill_switch = self.stop_now

                msg.header.frame_id = 'body'

            case 'heading':

                msg = Heading()

                msg.heading = self.heading

                msg.header.frame_id = 'earth'

        # Header

        msg.header.stamp = self.get_clock().now().to_msg()

        return msg
```