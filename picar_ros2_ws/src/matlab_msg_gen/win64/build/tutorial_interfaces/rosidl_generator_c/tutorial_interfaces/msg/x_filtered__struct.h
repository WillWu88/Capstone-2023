// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:msg\XFiltered.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__X_FILTERED__STRUCT_H_
#define TUTORIAL_INTERFACES__MSG__X_FILTERED__STRUCT_H_

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

// Struct defined in msg/XFiltered in the package tutorial_interfaces.
typedef struct tutorial_interfaces__msg__XFiltered
{
  std_msgs__msg__Header header;
  double xpos;
  double xvel;
} tutorial_interfaces__msg__XFiltered;

// Struct for a sequence of tutorial_interfaces__msg__XFiltered.
typedef struct tutorial_interfaces__msg__XFiltered__Sequence
{
  tutorial_interfaces__msg__XFiltered * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__msg__XFiltered__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__X_FILTERED__STRUCT_H_
