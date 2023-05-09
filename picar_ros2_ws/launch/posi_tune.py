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
            executable='kf',
            name='kf_fast'
        ),
        Node(
            package='picar_sys',
            executable='pid_posi',
            name='posi_ctrl'
        ),
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
    ])
