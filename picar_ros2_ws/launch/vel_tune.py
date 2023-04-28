from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='picar_sys',
            executable='motor',
            name='motor_mixer'
        ),
        Node(
            package='picar_sys',
            executable='pid_vel',
            name='velocity_control'
        ),
        Node(
            package='picar_sys',
            executable='test_pub',
            name='test_pub'
        ),
    ])
