// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:msg/RPM.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__RPM__BUILDER_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__RPM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/msg/detail/rpm__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace msg
{

namespace builder
{

class Init_RPM_rpmfiltered
{
public:
  explicit Init_RPM_rpmfiltered(::tutorial_interfaces::msg::RPM & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::msg::RPM rpmfiltered(::tutorial_interfaces::msg::RPM::_rpmfiltered_type arg)
  {
    msg_.rpmfiltered = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::msg::RPM msg_;
};

class Init_RPM_rpmraw
{
public:
  explicit Init_RPM_rpmraw(::tutorial_interfaces::msg::RPM & msg)
  : msg_(msg)
  {}
  Init_RPM_rpmfiltered rpmraw(::tutorial_interfaces::msg::RPM::_rpmraw_type arg)
  {
    msg_.rpmraw = std::move(arg);
    return Init_RPM_rpmfiltered(msg_);
  }

private:
  ::tutorial_interfaces::msg::RPM msg_;
};

class Init_RPM_header
{
public:
  Init_RPM_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RPM_rpmraw header(::tutorial_interfaces::msg::RPM::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_RPM_rpmraw(msg_);
  }

private:
  ::tutorial_interfaces::msg::RPM msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::msg::RPM>()
{
  return tutorial_interfaces::msg::builder::Init_RPM_header();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__RPM__BUILDER_HPP_
