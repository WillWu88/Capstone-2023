from setuptools import setup
import os

import rclpy
from rclpy.node import Node
package_name = 'picar_sys'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, 'drivers'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='willwu',
    maintainer_email='williamwu8-8@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'imu = picar_sys.imu_publisher:main',
            'test_sub = picar_sys.test_sub:main',
            'test_pub = picar_sys.test_pub:main',
            'rpm = picar_sys.rpm_publisher:main',
            'gps = picar_sys.gps_publisher:main',
            'kf = picar_sys.kalman_node:main',
            'pid_vel = picar_sys.pid_node:main',
            'pid_pose = picar_sys.pid_pose_node:main',
            'nav = picar_sys.navigation_publisher:main',
            'motor = picar_sys.motor_mixer:main',
            'steer = picar_sys.servo_node:main',
            'pid_posi = picar_sys.pid_position_node:main',
        ],
    },
)
