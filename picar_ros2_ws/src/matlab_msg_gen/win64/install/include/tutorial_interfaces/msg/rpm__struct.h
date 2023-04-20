// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:msg\RPM.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__RPM__STRUCT_H_
#define TUTORIAL_INTERFACES__MSG__RPM__STRUCT_H_

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

// Struct defined in msg/RPM in the package tutorial_interfaces.
typedef struct tutorial_interfaces__msg__RPM
{
  std_msgs__msg__Header header;
  double rpmraw;
  double rpmfiltered;
} tutorial_interfaces__msg__RPM;

// Struct for a sequence of tutorial_interfaces__msg__RPM.
typedef struct tutorial_interfaces__msg__RPM__Sequence
{
  tutorial_interfaces__msg__RPM * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__msg__RPM__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__RPM__STRUCT_H_
