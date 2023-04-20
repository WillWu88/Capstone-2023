from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='picar_sys',
            executable='imu',
            name='picar'
        ),
        Node(
            package='picar_sys',
            executable='rpm',
            name='picar'
        ),
        Node(
            package='picar_sys',
            executable='gps',
            name='picar'
        ),
    ])
