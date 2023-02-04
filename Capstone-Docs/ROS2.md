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

### 1.1.2 The Computation Graph

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

- Control application can be split into two different subsystems:
1) Behavior Subsystem: Made up of two ndes that collaborate to generate a robots behavior. Behavior coordinator (coordinator) and a node that impliments an active vision system (headController). The Coordinator determines where to look at and which points the robot should visit on a map.
2) Naviagtion Subsystem: Made up of several nodes. The navigation manager coordinates the planner (in charge of creating routes from the robot's position to the destination) and the controller (which makes the robot follow the created route). The planner needs the map provided by a node that shows the environmental map and the robot's position that calculates a location node.
-Communication between both subsystems is done with ROS2 actions. Actions are also used to coordinate the planner and controller within the navigation system.

### Key Takeaway for our Project: 

- Every time we impliment an action in ROS2, we design a computational graph. Establishing which nodes we need and what their interactions are. We must decide if a node is executed at a certain frequency or if some event causes its execution.

### 1.1.3 The Workspace

- The Workspace looks at ROS2 from a static point of view, where the ROS2 software is installed, organized, and all the tools and processes that allow us to launch a computing graph. 

- The fundamental element of the workspace is the package, which contains executables, libraries, or message definitions with a common purpose. 

- Another element is the workspace itself, where a workspace is a directory that contains packages. 

- There can be several workspaces in use at the same time, the inital workspace, underlay, and then any additional workspaces are referred to as overlay. 

- Packages can be installed from sources or with the systems installation system. Each ROS2 package is packaged in a deb package.

- Command
```shell
$ apt-cache seach ros-foxy
```

shows the packages available to install.

- Command
```shell
$ sudo rosdep init
$ rosdep update
Used to discover dependencies in packages not solved and installs them as deb packages.
```


- Sample of creating a workspace and adding packages on page 12.

- colcon (collective construction) is a command line tool for building, testing, and using multiple software packages. It automates the process of building and set up in the environment to use the packages. 

### Key Takeaways:
- Sums up how to set up a workspace and add packages to ROS2 workspace.

### 1.2 The ROS2 Design

- Packages which nodes and programs are implemented in C++ use the C++ client libraries, relepp, whereas packages in python use relpy.

- A crucial component of ROS2 is communications.

- ROS2 is a distributed system whose computing graph has nodes that can be spread over several machines.

- ROS2 chose DDS for its communication layer, more about that can be read in this chapter.

### 2.1 First Steps with ROS2

```shell
$ ros2 <command> <verb> [<params>|<option>]*
```
- ros2 is the main command in ros2, it allows interaction with the ROS2 system to obtain infomation or carry out actions.

```shell
$ ros2 pkg list
```
- A command used to obtain the list of available packages.

- ros2cli is the command line interface tool. It's modular and extensible, so that more functionality can be added by adding new actions.

```shell
$ ros2 pkg executables demo_nodes_cpp
```
- It is possible to get information on a specific package. For example, this code gets the executable programs for this cpp package.

```shell
$ ros2 run demo_nodes_cpp talker
```
- The run verb allows you to run arguments. and the word *talker* after the executable becomes the nodes name

```shell
$ ros2 node list
```
- Checks the nodes that are currently running.

```shell
$ ros2 topic list
```
- While a node is running, you can list the topics in the system.

```shell
$ ros2 node info /talker
```
- The info parameter gives more information on the system. This command will give the subscribers, publishers, and service servers for the node specified. 

```shell
$ ros2 topic info chatter
```
- Each topic supports messages of only one type. The topic command displays the type of the message, the publisher count, and the subscriber count.

```shell
$ ros2 topic echo /chatter
```
- To check the messages currently being published in a topic with the echo command.

```
$ ros2 run demo_nodes_py listener
```
- command to run the listener node that runs in python.

```shell
$ ros2 run rqt_graph rqt_graph
```
- It is possible to visualize the Computation Graph by running the rqt_graph tool which is in the rqt_graph package.

### 2.2 Developing the First Node

- All packages must be in the src directory

```shell
$ ros2 pkg create my_package --dependencies rclcpp std_msgs
```
- This command creates the skeleton of the basics package, with some empty directories to host the source files of our programs and libraries.
- ROS2 recognizes a directory contains a package because it has an XML file called package.xml.
- The --dependencies option allows you to add the dependencies of this package.

```C++
#include "rclcpp/rclcpp.hpp"

int main(int argc, char * argv[]){
	rclcpp::init(argc, argv);
	auto node = rclcpp::Node::make_shared("simple node");
	rclcpp::spin(node);
	rclcpp::shutdown();
	return 0;
}
```
- #include "rclcpp/rclcpp.hpp" allows access to most of the ROS2 types and functions in C++
- rclcpp::init(argc,argv) extracts from the arguments with which the process was launched any option should be taken into account by ROS2 
- Line 6 creates a ROS2 node (auto node), and named it simple node.
- The rclcpp::Node class is equipped with many aliases and static functions to simplify the code. 
- spin blocks the execution of the program so it doesn't terminate immediately.
- shutdown manages the shutdown of the node, prior to the end of the program in the next line.

- Identifying the parts of a built in text file (see CMakeLists.txt on page 26)
	- The packages needed are specified with find_package.
	- It is a good habit to create a dependencies variable with the packages that this package depends on since we will have to use that list several times.
	- Compile it: Done with add_executables, indiciating the name of the result and its sources.
	- Install it: Indiciate where to install the program produced, which generally doesn't vary; use a single install instruction.

```shell
colcon build --symlink-install
```
- Compiles the workspace.

### 2.3 Analyzing the BR2_BASICS Package

