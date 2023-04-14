// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from tutorial_interfaces:msg/GPS.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__GPS__STRUCT_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__GPS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__tutorial_interfaces__msg__GPS __attribute__((deprecated))
#else
# define DEPRECATED__tutorial_interfaces__msg__GPS __declspec(deprecated)
#endif

namespace tutorial_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct GPS_
{
  using Type = GPS_<ContainerAllocator>;

  explicit GPS_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->latitude_degrees = 0.0;
      this->longitude_degrees = 0.0;
      this->latitude_minutes = 0.0;
      this->longitude_minutes = 0.0;
      this->flag = false;
    }
  }

  explicit GPS_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->latitude_degrees = 0.0;
      this->longitude_degrees = 0.0;
      this->latitude_minutes = 0.0;
      this->longitude_minutes = 0.0;
      this->flag = false;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _latitude_degrees_type =
    double;
  _latitude_degrees_type latitude_degrees;
  using _longitude_degrees_type =
    double;
  _longitude_degrees_type longitude_degrees;
  using _latitude_minutes_type =
    double;
  _latitude_minutes_type latitude_minutes;
  using _longitude_minutes_type =
    double;
  _longitude_minutes_type longitude_minutes;
  using _flag_type =
    bool;
  _flag_type flag;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__latitude_degrees(
    const double & _arg)
  {
    this->latitude_degrees = _arg;
    return *this;
  }
  Type & set__longitude_degrees(
    const double & _arg)
  {
    this->longitude_degrees = _arg;
    return *this;
  }
  Type & set__latitude_minutes(
    const double & _arg)
  {
    this->latitude_minutes = _arg;
    return *this;
  }
  Type & set__longitude_minutes(
    const double & _arg)
  {
    this->longitude_minutes = _arg;
    return *this;
  }
  Type & set__flag(
    const bool & _arg)
  {
    this->flag = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    tutorial_interfaces::msg::GPS_<ContainerAllocator> *;
  using ConstRawPtr =
    const tutorial_interfaces::msg::GPS_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::GPS_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::GPS_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::GPS_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::GPS_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::GPS_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::GPS_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::GPS_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::GPS_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__tutorial_interfaces__msg__GPS
    std::shared_ptr<tutorial_interfaces::msg::GPS_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__tutorial_interfaces__msg__GPS
    std::shared_ptr<tutorial_interfaces::msg::GPS_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GPS_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->latitude_degrees != other.latitude_degrees) {
      return false;
    }
    if (this->longitude_degrees != other.longitude_degrees) {
      return false;
    }
    if (this->latitude_minutes != other.latitude_minutes) {
      return false;
    }
    if (this->longitude_minutes != other.longitude_minutes) {
      return false;
    }
    if (this->flag != other.flag) {
      return false;
    }
    return true;
  }
  bool operator!=(const GPS_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GPS_

// alias to use template instance with default allocator
using GPS =
  tutorial_interfaces::msg::GPS_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__GPS__STRUCT_HPP_
