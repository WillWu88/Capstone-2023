// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from tutorial_interfaces:msg\VelSetpoint.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__VEL_SETPOINT__TRAITS_HPP_
#define TUTORIAL_INTERFACES__MSG__VEL_SETPOINT__TRAITS_HPP_

#include "tutorial_interfaces/msg/vel_setpoint__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<tutorial_interfaces::msg::VelSetpoint>()
{
  return "tutorial_interfaces::msg::VelSetpoint";
}

template<>
struct has_fixed_size<tutorial_interfaces::msg::VelSetpoint>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<tutorial_interfaces::msg::VelSetpoint>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

}  // namespace rosidl_generator_traits

#endif  // TUTORIAL_INTERFACES__MSG__VEL_SETPOINT__TRAITS_HPP_
