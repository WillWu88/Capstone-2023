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
        ),
        Node(
            package='picar_sys',
            executable='kf',
            name='kalman_filter'
        ),
        Node(
            package='picar_sys',
            executable='nav',
            name='navigator'
        ),
        Node(
            package='picar_sys',
            executable='pid_vel',
            name='velocity_control'
        ),
        Node(
            package='picar_sys',
            executable='pid_pose',
            name='pose_control'
        ),
    ])
