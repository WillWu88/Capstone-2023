// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from tutorial_interfaces:msg\XFiltered.idl
// generated code does not contain a copyright notice
#include "tutorial_interfaces/msg/x_filtered__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header__functions.h"

bool
tutorial_interfaces__msg__XFiltered__init(tutorial_interfaces__msg__XFiltered * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    tutorial_interfaces__msg__XFiltered__destroy(msg);
    return false;
  }
  // xpos
  // xvel
  return true;
}

void
tutorial_interfaces__msg__XFiltered__fini(tutorial_interfaces__msg__XFiltered * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // xpos
  // xvel
}

tutorial_interfaces__msg__XFiltered *
tutorial_interfaces__msg__XFiltered__create()
{
  tutorial_interfaces__msg__XFiltered * msg = (tutorial_interfaces__msg__XFiltered *)malloc(sizeof(tutorial_interfaces__msg__XFiltered));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(tutorial_interfaces__msg__XFiltered));
  bool success = tutorial_interfaces__msg__XFiltered__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
tutorial_interfaces__msg__XFiltered__destroy(tutorial_interfaces__msg__XFiltered * msg)
{
  if (msg) {
    tutorial_interfaces__msg__XFiltered__fini(msg);
  }
  free(msg);
}


bool
tutorial_interfaces__msg__XFiltered__Sequence__init(tutorial_interfaces__msg__XFiltered__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  tutorial_interfaces__msg__XFiltered * data = NULL;
  if (size) {
    data = (tutorial_interfaces__msg__XFiltered *)calloc(size, sizeof(tutorial_interfaces__msg__XFiltered));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = tutorial_interfaces__msg__XFiltered__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        tutorial_interfaces__msg__XFiltered__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
tutorial_interfaces__msg__XFiltered__Sequence__fini(tutorial_interfaces__msg__XFiltered__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      tutorial_interfaces__msg__XFiltered__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

tutorial_interfaces__msg__XFiltered__Sequence *
tutorial_interfaces__msg__XFiltered__Sequence__create(size_t size)
{
  tutorial_interfaces__msg__XFiltered__Sequence * array = (tutorial_interfaces__msg__XFiltered__Sequence *)malloc(sizeof(tutorial_interfaces__msg__XFiltered__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = tutorial_interfaces__msg__XFiltered__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
tutorial_interfaces__msg__XFiltered__Sequence__destroy(tutorial_interfaces__msg__XFiltered__Sequence * array)
{
  if (array) {
    tutorial_interfaces__msg__XFiltered__Sequence__fini(array);
  }
  free(array);
}
