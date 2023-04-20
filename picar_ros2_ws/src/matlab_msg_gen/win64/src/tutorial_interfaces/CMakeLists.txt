cmake_minimum_required(VERSION 3.5)
project(tutorial_interfaces)
# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()
# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()
# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_ros REQUIRED)
find_package(rosidl_typesupport_c REQUIRED)
find_package(rosidl_typesupport_cpp REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package( class_loader REQUIRED)
find_package( console_bridge REQUIRED)
find_package( rclcpp REQUIRED)
find_package( rcutils REQUIRED)
find_package( std_msgs REQUIRED)
include_directories("C:/Program Files/MATLAB/R2021a/extern/include")
include_directories("C:/Program Files/MATLAB/R2021a/extern/include/MatlabDataArray")
include_directories("C:/Program Files/MATLAB/R2021a/toolbox/ros/include/ros2")
include_directories("include/tutorial_interfaces")
set (CMAKE_SKIP_BUILD_RPATH false)
set (CMAKE_BUILD_WITH_INSTALL_RPATH true)
set (CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
set(msg_files
  "msg/GPS.msg"
  "msg/PoseSetpoint.msg"
  "msg/RPM.msg"
  "msg/VelSetpoint.msg"
  "msg/XFiltered.msg"
  "msg/YFiltered.msg"
  "msg/YawFiltered.msg"
)
rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
  DEPENDENCIES 
  std_msgs
)
link_directories("C:/Program Files/MATLAB/R2021a/extern/lib/win64/microsoft")
# Library
add_library(
    tutorial_interfaces_matlab 
    SHARED
    src/tutorial_interfaces_GPS_message.cpp
    src/tutorial_interfaces_PoseSetpoint_message.cpp
    src/tutorial_interfaces_RPM_message.cpp
    src/tutorial_interfaces_VelSetpoint_message.cpp
    src/tutorial_interfaces_XFiltered_message.cpp
    src/tutorial_interfaces_YFiltered_message.cpp
    src/tutorial_interfaces_YawFiltered_message.cpp
)
target_include_directories(tutorial_interfaces_matlab PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_link_libraries( tutorial_interfaces_matlab
	libMatlabDataArray
	${CMAKE_DL_LIBS}
	)
ament_target_dependencies(
  tutorial_interfaces_matlab
  "class_loader"
  "console_bridge"
  "rclcpp"
  "rcutils"
  "std_msgs"
)
rosidl_target_interfaces(
	  tutorial_interfaces_matlab
      ${PROJECT_NAME} "rosidl_typesupport_cpp")
# Causes the visibility macros to use dllexport rather than dllimport,
# which is appropriate when building the dll but not consuming it.
target_compile_definitions(tutorial_interfaces_matlab PRIVATE "TUTORIAL_INTERFACES_BUILDING_LIBRARY")
install(
  DIRECTORY include/
  DESTINATION include
)
install(
  TARGETS tutorial_interfaces_matlab
  EXPORT export_${PROJECT_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)
install (DIRECTORY m/ DESTINATION m/ FILES_MATCHING PATTERN "*.m")
ament_export_include_directories(
  include
)
ament_export_libraries(
  tutorial_interfaces_matlab
)
ament_package()
# Generated 19-Apr-2023 19:08:59
# Copyright 2019-2020 The MathWorks, Inc.
