// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from tutorial_interfaces:msg/GPS.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__GPS__TRAITS_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__GPS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "tutorial_interfaces/msg/detail/gps__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace tutorial_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const GPS & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: latitude_degrees
  {
    out << "latitude_degrees: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude_degrees, out);
    out << ", ";
  }

  // member: longitude_degrees
  {
    out << "longitude_degrees: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude_degrees, out);
    out << ", ";
  }

  // member: latitude_minutes
  {
    out << "latitude_minutes: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude_minutes, out);
    out << ", ";
  }

  // member: longitude_minutes
  {
    out << "longitude_minutes: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude_minutes, out);
    out << ", ";
  }

  // member: flag
  {
    out << "flag: ";
    rosidl_generator_traits::value_to_yaml(msg.flag, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GPS & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: latitude_degrees
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "latitude_degrees: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude_degrees, out);
    out << "\n";
  }

  // member: longitude_degrees
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "longitude_degrees: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude_degrees, out);
    out << "\n";
  }

  // member: latitude_minutes
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "latitude_minutes: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude_minutes, out);
    out << "\n";
  }

  // member: longitude_minutes
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "longitude_minutes: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude_minutes, out);
    out << "\n";
  }

  // member: flag
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flag: ";
    rosidl_generator_traits::value_to_yaml(msg.flag, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GPS & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace tutorial_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use tutorial_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const tutorial_interfaces::msg::GPS & msg,
  std::ostream & out, size_t indentation = 0)
{
  tutorial_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use tutorial_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const tutorial_interfaces::msg::GPS & msg)
{
  return tutorial_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<tutorial_interfaces::msg::GPS>()
{
  return "tutorial_interfaces::msg::GPS";
}

template<>
inline const char * name<tutorial_interfaces::msg::GPS>()
{
  return "tutorial_interfaces/msg/GPS";
}

template<>
struct has_fixed_size<tutorial_interfaces::msg::GPS>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<tutorial_interfaces::msg::GPS>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<tutorial_interfaces::msg::GPS>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__GPS__TRAITS_HPP_
