// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:msg/GPS.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__GPS__BUILDER_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__GPS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/msg/detail/gps__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace msg
{

namespace builder
{

class Init_GPS_flag
{
public:
  explicit Init_GPS_flag(::tutorial_interfaces::msg::GPS & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::msg::GPS flag(::tutorial_interfaces::msg::GPS::_flag_type arg)
  {
    msg_.flag = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::msg::GPS msg_;
};

class Init_GPS_longitude_minutes
{
public:
  explicit Init_GPS_longitude_minutes(::tutorial_interfaces::msg::GPS & msg)
  : msg_(msg)
  {}
  Init_GPS_flag longitude_minutes(::tutorial_interfaces::msg::GPS::_longitude_minutes_type arg)
  {
    msg_.longitude_minutes = std::move(arg);
    return Init_GPS_flag(msg_);
  }

private:
  ::tutorial_interfaces::msg::GPS msg_;
};

class Init_GPS_latitude_minutes
{
public:
  explicit Init_GPS_latitude_minutes(::tutorial_interfaces::msg::GPS & msg)
  : msg_(msg)
  {}
  Init_GPS_longitude_minutes latitude_minutes(::tutorial_interfaces::msg::GPS::_latitude_minutes_type arg)
  {
    msg_.latitude_minutes = std::move(arg);
    return Init_GPS_longitude_minutes(msg_);
  }

private:
  ::tutorial_interfaces::msg::GPS msg_;
};

class Init_GPS_longitude_degrees
{
public:
  explicit Init_GPS_longitude_degrees(::tutorial_interfaces::msg::GPS & msg)
  : msg_(msg)
  {}
  Init_GPS_latitude_minutes longitude_degrees(::tutorial_interfaces::msg::GPS::_longitude_degrees_type arg)
  {
    msg_.longitude_degrees = std::move(arg);
    return Init_GPS_latitude_minutes(msg_);
  }

private:
  ::tutorial_interfaces::msg::GPS msg_;
};

class Init_GPS_latitude_degrees
{
public:
  explicit Init_GPS_latitude_degrees(::tutorial_interfaces::msg::GPS & msg)
  : msg_(msg)
  {}
  Init_GPS_longitude_degrees latitude_degrees(::tutorial_interfaces::msg::GPS::_latitude_degrees_type arg)
  {
    msg_.latitude_degrees = std::move(arg);
    return Init_GPS_longitude_degrees(msg_);
  }

private:
  ::tutorial_interfaces::msg::GPS msg_;
};

class Init_GPS_header
{
public:
  Init_GPS_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GPS_latitude_degrees header(::tutorial_interfaces::msg::GPS::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_GPS_latitude_degrees(msg_);
  }

private:
  ::tutorial_interfaces::msg::GPS msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::msg::GPS>()
{
  return tutorial_interfaces::msg::builder::Init_GPS_header();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__GPS__BUILDER_HPP_
