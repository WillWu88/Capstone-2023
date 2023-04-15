// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from tutorial_interfaces:msg/RPM.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__RPM__TRAITS_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__RPM__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "tutorial_interfaces/msg/detail/rpm__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace tutorial_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const RPM & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: rpmraw
  {
    out << "rpmraw: ";
    rosidl_generator_traits::value_to_yaml(msg.rpmraw, out);
    out << ", ";
  }

  // member: rpmfiltered
  {
    out << "rpmfiltered: ";
    rosidl_generator_traits::value_to_yaml(msg.rpmfiltered, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RPM & msg,
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

  // member: rpmraw
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rpmraw: ";
    rosidl_generator_traits::value_to_yaml(msg.rpmraw, out);
    out << "\n";
  }

  // member: rpmfiltered
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rpmfiltered: ";
    rosidl_generator_traits::value_to_yaml(msg.rpmfiltered, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RPM & msg, bool use_flow_style = false)
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
  const tutorial_interfaces::msg::RPM & msg,
  std::ostream & out, size_t indentation = 0)
{
  tutorial_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use tutorial_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const tutorial_interfaces::msg::RPM & msg)
{
  return tutorial_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<tutorial_interfaces::msg::RPM>()
{
  return "tutorial_interfaces::msg::RPM";
}

template<>
inline const char * name<tutorial_interfaces::msg::RPM>()
{
  return "tutorial_interfaces/msg/RPM";
}

template<>
struct has_fixed_size<tutorial_interfaces::msg::RPM>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<tutorial_interfaces::msg::RPM>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<tutorial_interfaces::msg::RPM>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__RPM__TRAITS_HPP_
