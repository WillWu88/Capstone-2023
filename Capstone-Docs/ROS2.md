#ros2

## Robotic Operating System, Version 2

## Useful Commands

- `rosdep`, a ros package dependency installer
```shell
rosdep update
rosdep -h # read the documentation
```




## Appendix: References

- [Robotics Back-end tutorials](https://roboticsbackend.com/category/ros2/)
- [Official ROS Documentation](https://docs.ros.org/en/humble/index.html)

## Textbook Notes

1.1.2 The Computation Graph

-A computation Graph contains ROS2 nodes that communicate with eachother so the robot can carry out tasks, the logic of the application is in the nodes, as the primary element of execution.

-ROS2 uses Object Oriented Programing, where a node is an object of class Node.

-A node can access the Computation Graph and provides mechanisms to commuicate with other nodes:
1) Publication/Subscription: Asynchronous communication where N nodes publish messages to a topic(a communication channel that accepts messages of a unique type) that reaches its M subscribers. I.e. when nodes need images from a camera that publishes its images, those nodes subscribe to that topic.
2) Services: Synchronous communication where a node requests another node and then waits for the response, this often requires an immediate response. I.e requesting a mapping service to reset a map, with a response indicating if the call succeeds. 
3) Actions: Asychronous communcation where a node makes a request to another node in which the request takes time to complete or may periodically receive feedback. I.e navigation, since this is time consuming the request shouldn't block other actions.

-Nodes in a computational graph are meant to perform processing or control. They are therefore considered active elements with some alternatives in terms of their execution model:
1) Iterative Execution: When a node executes its control cycle at a specific frequency. Allows for controlling how many computational resources a node requires, and the output flow remains constant.
2) Event-oriented execution: Where execution of nodes is determined by the frequency at which certain events occur, in one case, the arrival of messages at the node. 

-Kobuki Robot example of different execution types and subscription to nodes, on pages 7&8.

-Control application can be split into two different subsystems:
1) Behavior Subsystem: Made up of two ndes that collaborate to generate a robots behavior. Behavior coordinator (coordinator) and a node that impliments an active vision system (headController). The Coordinator determines where to look at and which points the robot should visit on a map.
2) Naviagtion Subsystem: Made up of several nodes. The navigation manager coordinates the planner (in charge of creating routes from the robot's position to the destination) and the controller (which makes the robot follow the created route). The planner needs the map provided by a node that shows the environmental map and the robot's position that calculates a location node.
-Communication between both subsystems is done with ROS2 actions. Actions are also used to coordinate the planner and controller within the navigation system.

Key Takeaway for our Project: 

-Every time we impliment an action in ROS2, we design a computational graph. Establishing which nodes we need and what their interactions are. We must decide if a node is executed at a certain frequency or if some event causes its execution.

1.1.3 The Workspace