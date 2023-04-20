// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:msg\YawFiltered.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__YAW_FILTERED__STRUCT_H_
#define TUTORIAL_INTERFACES__MSG__YAW_FILTERED__STRUCT_H_

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

// Struct defined in msg/YawFiltered in the package tutorial_interfaces.
typedef struct tutorial_interfaces__msg__YawFiltered
{
  std_msgs__msg__Header header;
  double yawpos;
  double yawvel;
} tutorial_interfaces__msg__YawFiltered;

// Struct for a sequence of tutorial_interfaces__msg__YawFiltered.
typedef struct tutorial_interfaces__msg__YawFiltered__Sequence
{
  tutorial_interfaces__msg__YawFiltered * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__msg__YawFiltered__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__YAW_FILTERED__STRUCT_H_
