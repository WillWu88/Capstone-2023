from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='picar_sys',
            executable='imu',
            name='imu'
        ),
        Node(
            package='picar_sys',
            executable='rpm',
            name='rpm'
        ),
        Node(
            package='picar_sys',
            executable='gps',
            name='gps'
        )
    ])
