// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:msg\PoseSetpoint.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__POSE_SETPOINT__STRUCT_H_
#define TUTORIAL_INTERFACES__MSG__POSE_SETPOINT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/header__struct.h"

// Struct defined in msg/PoseSetpoint in the package tutorial_interfaces.
typedef struct tutorial_interfaces__msg__PoseSetpoint
{
  std_msgs__msg__Header header;
  double yawsetpoint;
} tutorial_interfaces__msg__PoseSetpoint;

// Struct for a sequence of tutorial_interfaces__msg__PoseSetpoint.
typedef struct tutorial_interfaces__msg__PoseSetpoint__Sequence
{
  tutorial_interfaces__msg__PoseSetpoint * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__msg__PoseSetpoint__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__POSE_SETPOINT__STRUCT_H_
