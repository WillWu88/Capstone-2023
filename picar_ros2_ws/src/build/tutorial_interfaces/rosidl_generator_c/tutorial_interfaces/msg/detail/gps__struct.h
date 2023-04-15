// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:msg/GPS.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__GPS__STRUCT_H_
#define TUTORIAL_INTERFACES__MSG__DETAIL__GPS__STRUCT_H_

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
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/GPS in the package tutorial_interfaces.
typedef struct tutorial_interfaces__msg__GPS
{
  std_msgs__msg__Header header;
  double latitude_degrees;
  double longitude_degrees;
  double latitude_minutes;
  double longitude_minutes;
  bool flag;
} tutorial_interfaces__msg__GPS;

// Struct for a sequence of tutorial_interfaces__msg__GPS.
typedef struct tutorial_interfaces__msg__GPS__Sequence
{
  tutorial_interfaces__msg__GPS * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__msg__GPS__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__GPS__STRUCT_H_
