// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:msg\RPM.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__RPM__FUNCTIONS_H_
#define TUTORIAL_INTERFACES__MSG__RPM__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_generator_c/visibility_control.h"
#include "tutorial_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "tutorial_interfaces/msg/rpm__struct.h"

/// Initialize msg/RPM message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * tutorial_interfaces__msg__RPM
 * )) before or use
 * tutorial_interfaces__msg__RPM__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
bool
tutorial_interfaces__msg__RPM__init(tutorial_interfaces__msg__RPM * msg);

/// Finalize msg/RPM message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
void
tutorial_interfaces__msg__RPM__fini(tutorial_interfaces__msg__RPM * msg);

/// Create msg/RPM message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * tutorial_interfaces__msg__RPM__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
tutorial_interfaces__msg__RPM *
tutorial_interfaces__msg__RPM__create();

/// Destroy msg/RPM message.
/**
 * It calls
 * tutorial_interfaces__msg__RPM__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
void
tutorial_interfaces__msg__RPM__destroy(tutorial_interfaces__msg__RPM * msg);


/// Initialize array of msg/RPM messages.
/**
 * It allocates the memory for the number of elements and calls
 * tutorial_interfaces__msg__RPM__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
bool
tutorial_interfaces__msg__RPM__Sequence__init(tutorial_interfaces__msg__RPM__Sequence * array, size_t size);

/// Finalize array of msg/RPM messages.
/**
 * It calls
 * tutorial_interfaces__msg__RPM__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
void
tutorial_interfaces__msg__RPM__Sequence__fini(tutorial_interfaces__msg__RPM__Sequence * array);

/// Create array of msg/RPM messages.
/**
 * It allocates the memory for the array and calls
 * tutorial_interfaces__msg__RPM__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
tutorial_interfaces__msg__RPM__Sequence *
tutorial_interfaces__msg__RPM__Sequence__create(size_t size);

/// Destroy array of msg/RPM messages.
/**
 * It calls
 * tutorial_interfaces__msg__RPM__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
void
tutorial_interfaces__msg__RPM__Sequence__destroy(tutorial_interfaces__msg__RPM__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__RPM__FUNCTIONS_H_
