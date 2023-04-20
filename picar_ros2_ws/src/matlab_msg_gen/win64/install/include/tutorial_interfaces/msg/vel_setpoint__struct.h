// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:msg\VelSetpoint.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__VEL_SETPOINT__STRUCT_H_
#define TUTORIAL_INTERFACES__MSG__VEL_SETPOINT__STRUCT_H_

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

// Struct defined in msg/VelSetpoint in the package tutorial_interfaces.
typedef struct tutorial_interfaces__msg__VelSetpoint
{
  std_msgs__msg__Header header;
  double xvelsetpoint;
  double yvelsetpoint;
} tutorial_interfaces__msg__VelSetpoint;

// Struct for a sequence of tutorial_interfaces__msg__VelSetpoint.
typedef struct tutorial_interfaces__msg__VelSetpoint__Sequence
{
  tutorial_interfaces__msg__VelSetpoint * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__msg__VelSetpoint__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__VEL_SETPOINT__STRUCT_H_
