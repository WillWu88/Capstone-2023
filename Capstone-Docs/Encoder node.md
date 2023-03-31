#programming #ros2 #sensor #design 

## I. Node service

## II. Node publisher

The publisher node publishes data for the subscriber to the topic to receive. The first lines of our code imports rclpy which implements the ROS client interface routines and its Node class.

``` python
import rclpy
from rclpy.node import Node
```

In a separate package we created a built-in message type , which we import to structure the data that passes on the topic.

```python
from tutorial_interfaces.msg import Rpmmsg
```

Next, the RpmPublisher class is created, which is a subclass of Node.

```python
class RpmPublisher(Node)
```

Calling the following line defines the class's constructor and gives the node a name:

```python
super().__init__('rpm_publisher')
```

The class's constructor:

```python
def __init__(self):
    super().__init__('rpm_publisher')
    self.publisher_ = self.create_publisher(String, 'topic', 10)
    timer_period = 0.005  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
```
The publisher sends a message at a frequency of 200 Hz (every 0.005 s).  




## III. Node subscriber



## Appendix References:
- [ROS 2 documentation: Understanding services](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html)
- [ROS 2 documentation: tutorial on how to create a publisher](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)

- [ROS 2 documentation: creating custom msg and srv files](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html)