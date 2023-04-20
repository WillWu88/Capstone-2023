// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from tutorial_interfaces:msg\GPS.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__GPS__STRUCT_HPP_
#define TUTORIAL_INTERFACES__MSG__GPS__STRUCT_HPP_

#include <rosidl_generator_cpp/bounded_vector.hpp>
#include <rosidl_generator_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/header__struct.hpp"

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

  explicit GPS_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->latdeg = 0.0;
      this->longdeg = 0.0;
      this->latmin = 0.0;
      this->longmin = 0.0;
      this->flag = false;
    }
  }

  explicit GPS_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->latdeg = 0.0;
      this->longdeg = 0.0;
      this->latmin = 0.0;
      this->longmin = 0.0;
      this->flag = false;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _latdeg_type =
    double;
  _latdeg_type latdeg;
  using _longdeg_type =
    double;
  _longdeg_type longdeg;
  using _latmin_type =
    double;
  _latmin_type latmin;
  using _longmin_type =
    double;
  _longmin_type longmin;
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
  Type & set__latdeg(
    const double & _arg)
  {
    this->latdeg = _arg;
    return *this;
  }
  Type & set__longdeg(
    const double & _arg)
  {
    this->longdeg = _arg;
    return *this;
  }
  Type & set__latmin(
    const double & _arg)
  {
    this->latmin = _arg;
    return *this;
  }
  Type & set__longmin(
    const double & _arg)
  {
    this->longmin = _arg;
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
    if (this->latdeg != other.latdeg) {
      return false;
    }
    if (this->longdeg != other.longdeg) {
      return false;
    }
    if (this->latmin != other.latmin) {
      return false;
    }
    if (this->longmin != other.longmin) {
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

#endif  // TUTORIAL_INTERFACES__MSG__GPS__STRUCT_HPP_
