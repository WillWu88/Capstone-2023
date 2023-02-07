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

#### 2.3.1 Controlling the Iterative Execution

```C++
auto node = rclcpp::Node::make_shared(logger_node);

rclcpp::Rate loop_rate(500ms);
int counter = 0;
while (rclcpp::ok()){
	RCLCPP_INFO(node->get_logger(), "Hello %d", counter++);
	rclcpp::spin_some(node);
	loop_rate.sleep();
}
```
- This code shows the first of the typical strategy to perform a task at a fixed frequency, which is common in any program that performs some control.
- The control loop is made in the while loop , controlling the rate with the rclcpp::Rate object.
- This code uses spin_some instead of spin, both are to manage messages that arrive at the node, calling the functions that should handle them. While spin blocks wait for new messages, spin_some returns when there are no messages left to handle.

```shell
$ ros2 run rqt_console rqt_console
```
- This tool shows the messages that are published in /rosout.

- There is a second strategy to iteratively execute a task can be seen in the src/logger_class.cpp program (seen on page 31).
	- This approach allows to have a cleaner code and opens the door to many possibilities that will be shown later.
	- A timer controls the control loop, producing an event at the desired frequency.
	- When this event happens, it calls the callback that handles it.
	- Schedule the nodes to see how often they should run

#### 2.3.2 Publishing and Subscribing

```C++
class PublisherNode : public rclcpp::Node
{
public:
	PublisherNode() : Node("publisher_node")
	{
	publisher = create_publisher<std_msgs::msg::Int32>("int_topic",10);
	timer = create_wall_timer(500ms, std::bind(&PublisherNode::timer_callback, this));
	}
	void timer_callback();
	{
	message_.data += 1;
	publisher_->publish(message);
	}
private:
	rclcpp::Publisher,std_msgs::msg::Int32>("int_topic",10);
	rclcpp::TimerBase::SharedPtr timer_;
	std_msgs::msg::Int32 message_;
}
```
- We will use the std_msgs/msg/Int32 message:
	- Its header is std_msgs/msg/int32.hpp
	- The data type is std_msgs::msg::Int32
- Creates a publisher, the object in charge of creating the topic and publishing messages. 
- We use create_publisher, which is a public method of rclcpp::Node, and it returns a shared_ptr to an rclcpp::Publisher object. The arguments are the name of the topic and an rclcpp::QoS object.
- We create a std_msgs::msg::Int32 message, which we can verify only has one data field, and every 500ms, in the timer callback, we intrement the message field and call the publisher's publish method to publish the message.

- QoS in ROS2 is an essential and valuable feature, the durablility and reliability profiles as well as other QoS features on page 34.

```shell
$ ros2 run br2_basics publisher_class
```
- runs the program and displays what is being published.

```C++
class SubscriberNode : public rclcpp::Node
{
public:
	SubscriberNode() : Node("subscriber_node")
	{
		subscriber = create_subscription<stdmsgs:msg:Int32>("int_topic", 10, std::bind(&SubscriberNode::callback, this, _1);
	}
	void callback(const std_msgs::msg::Int32::SharedPtr msg)
	{
		RCLCPP_INFO(get_logger(), "Hello %d", msg->data);
	}
private:
	rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr subscriber_;
};
```
- Creates a subscription to the same topic, with the same type of messages.

```shell
$ ros2 run br2_basics subscriber_class
```
- runs the subscriber class.

#### 2.3.3 Launchers

- So far we have seen programs run with ros2 run, however there is another way to run programs through the command ros2 launch, and using a file called launcher, that specifies which programs should be run.

- The launcher files are written in Python and their function is declaring which programs to execute with which options or arguments.

- The need for launchers comes from the fact tat a robotic application has many nodes, and they should all be launched simultaneously.

- Launchers for a package are located in the launch directory of a package, and their name usually ends in _launch.py.

```shell
$ ros2 launch
```
- completes the programs with available launchers.

- A launcher is a python program that contains a generate_launch_description() function that returns a LaunchDescription object, which contains:
	- Node action: to run a program
	- IncludeLaunchDescription action: to include another launcher
	- DeclareLaunchArgument action: to declare launcher parameters
	- SetEnvironmentVariable action: to set an environment variable

- To see how we can launch a publisher and subscriber at the same time, analyze the first launcer in the basics package (pg 36).

#### 2.3.4 Parameters

- A node uses the parameters to configure its operation. 

- Parameters are read at run time, usually when a node starts, and their operation depends on these values.

- Create a param_reader.cpp file in the basics package. (pg 37)
	- All parameters of a node must be decalred using methods like declare parameter. In the declaration, we specify the parameter name and the default value.
	- We obtain its value with functions like get_parameter, specifying the name of the parameter and where to store its value.
	- There are methods to do this in blocks.
	- The parameters can be read at any time, even subscribe to modifications in real time. However, reading them to the startup makes yout code more predictable.

```shell
$ ros2 run br2_basics param_reader
```
- running the program without setting parameter values

- It is usually convenient to use a file containing the parameters' values with which wwe want to execute a node. 

#### 2.3.5 Executors

- ROS2 offers you several ways to run multiple nodes in the same process, the most recommended is to make use of executors.

- An Executor is an object to which nodes are added to execute them together. 

- See examples of single and multi thread executors (pg 40)

### 2.4 Simulated Robot Setup

- This section walks through using the Kobuki Robot, which will have minimal applications for our project.

### 3.1 Perception and Actuation Models

- ROS2 uses the metric system of measurements (SI). For different dimensions, we will consider the units of meters, seconds, and radians.

- In ROS2 we are right-handed: x grows forward, y to the left, and z grows up. 

- Angles are defined as rotations around the axes. Rotation around x is something called the roll, y pitch, and z yaw.

- Angles grow by turning to the left. Angle 0 is forward , pi is back, and pi/2 is left

- Talks about the outputs of a lazer, not applicable to our project. 

- An essential feature of ROS is standardization.

### 3.2 Computation Graph

- The control logic interprets the input sensory information and produces the control commands.

- This logic is what we implement with an FSM.

- A good approach is that if the number of publishers and subscribers in a node is known, use generic topic names, like the ones used in this example, and perform a remap.

- A seasoned ROS2 programmer will read in the documentation, what topics it uses, find out with a ros2 node info, and quickly make work with remaps, instead of looking for the correct parameters to be set up in the configuration files.

### 3.3.1 Execution Control

- The node execution model consists of calling the control_cycle method at the selected frequency.
	- To do this we declare a timer and start it in the constructor to call the control_cycle method every 50 ms.
	- The control logic, implemented with an FSM, will publish the commands in speeds.

- The Callbacks in ROS2 can have different signatures , depending on the needs.
	- Some signatures allow to obtain information about the message (timestamp in origin and destination, and identifier of the sender) and even the serialized message, but that is only used in very specialized cases.

- As a general rule, for a communication to be compatible, the quality of service of the publisher should be reliable, and it is the subscriber who can choose to relax it to be the best effort.

### 3.3.2 Implementing a FSM

- Sample FSM code pg 55 is for C++

- Uses switch state to decide the state of the FSM

### 3.3.3 Running the Code

- Walks though steps for running books sample code

### 3.4 Bump and Go Behavior in Python

```shell
$ ros2 pkg create --build-type ament_python br2_fsm_bumpgo_py --dependencies sensor_msgs geometry_msgs
```
- To create a skeleton.

### 3.4.1 Execution Control

- Displays python sample code
	- Our code will have a subscriber, a publisher, and a timer
	- Has a walkthrough of features of the sample code

### 3.4.2 Implementing the FSM

- Sample code for communicating with the clock to get the time

- Code Notes:
	- The Time.from_msg function allows to create a Time object from the timestamp of a message.
	- The current time is obtained with Nodes get.clock().now() method.
	- The operation between time has as a result an object of type Duration, which can be compared with another object of type Duration that represents the duration of 2s.

### 3.4.3 Running the Code

```shell
$ colcon build --symlink-install
```
- Add a package needed for the sample code

```shell
$ ros2 launch br2_tiago sim.launch.py
```
- Launches the simulator.

```shell
$ ros2 run br2_fsm_bumpgo_py bump_go_main --ros-args -r output_vel:=/nav_vel -r input_scan:=/scan_raw -p use_sim_time:=true
```
- Run the program in another terminal

```shell
$ ros2 launch br2_fsm_bumpgo_py bump_and_go.launch.py
```
- Another launcher option