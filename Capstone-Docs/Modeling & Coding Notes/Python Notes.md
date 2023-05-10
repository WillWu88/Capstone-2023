#programming 

## Topics

#### 1. Super Init

- Super init
	- [Reference](https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods)
	- Note: 
	- Code example
```python
def __init__(self):
	super().__init__()
```

#### 2. Python Build System

- Important pieces: `setup.py`, `setup.cfg`, `__init__.py`, `__main__.py`
	- `__init.py__` recognize directory as packages

- Include files in a python project
	- File strucutre:
```Shell
➜  picar_sys git:(main) ✗ tree ..
..
├── package.xml
├── drivers
│   ├── __init__.py
│   ├── car_param.py
│   ├── encoder_driver.py
│   ├── encoder_driver.py
│   ├── gps_driver.py
│   ├── gps_helper.py
│   ├── imu_driver.py
│   ├── imu_param.py
│   ├── kf_constants.py
│   ├── motor_driver.py
│   ├── navigation_points.py
│   ├──pid_constant.py
│   ├── pid_driver.py
│   ├── rpm_serial_driver.py
│   ├── steer_driver.py
├── picar_sys
│   ├── rpm_publisher.py
│   ├── navigation_publisher.py
│   ├── servo_node.py
│   ├── pid_node.py
│   ├── pid_pose_node.py
│   ├── kalman_node.py
│   ├── motor_mixer.py
│   ├── imu_publisher.py
│   ├── __init__.py
│   ├── test_pub.py
│   ├── test_sub.py
│   └── __pycache__
│       ├── imu_driver.cpython-310.pyc
│       └── imu_param.cpython-310.pyc
├── resource
│   └── picar_sys
├── setup.cfg
├── setup.py
└── test
    ├── test_copyright.py
    ├── test_flake8.py
    └── test_pep257.py
```

- Include package as follows:
```python
import picar_sys.imu_driver
# note the prepended picar_sys 
```
- [Documentation]([python - What is __init__.py for? - Stack Overflow](https://stackoverflow.com/questions/448271/what-is-init-py-for))

#### 3. Specifying return types

```python
def function(arg) -> return_class:
	pass
```

