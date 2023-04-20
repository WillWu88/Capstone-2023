// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from tutorial_interfaces:msg\VelSetpoint.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__VEL_SETPOINT__STRUCT_HPP_
#define TUTORIAL_INTERFACES__MSG__VEL_SETPOINT__STRUCT_HPP_

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
# define DEPRECATED__tutorial_interfaces__msg__VelSetpoint __attribute__((deprecated))
#else
# define DEPRECATED__tutorial_interfaces__msg__VelSetpoint __declspec(deprecated)
#endif

namespace tutorial_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct VelSetpoint_
{
  using Type = VelSetpoint_<ContainerAllocator>;

  explicit VelSetpoint_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->xvelsetpoint = 0.0;
      this->yvelsetpoint = 0.0;
    }
  }

  explicit VelSetpoint_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->xvelsetpoint = 0.0;
      this->yvelsetpoint = 0.0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _xvelsetpoint_type =
    double;
  _xvelsetpoint_type xvelsetpoint;
  using _yvelsetpoint_type =
    double;
  _yvelsetpoint_type yvelsetpoint;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__xvelsetpoint(
    const double & _arg)
  {
    this->xvelsetpoint = _arg;
    return *this;
  }
  Type & set__yvelsetpoint(
    const double & _arg)
  {
    this->yvelsetpoint = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator> *;
  using ConstRawPtr =
    const tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__tutorial_interfaces__msg__VelSetpoint
    std::shared_ptr<tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__tutorial_interfaces__msg__VelSetpoint
    std::shared_ptr<tutorial_interfaces::msg::VelSetpoint_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const VelSetpoint_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->xvelsetpoint != other.xvelsetpoint) {
      return false;
    }
    if (this->yvelsetpoint != other.yvelsetpoint) {
      return false;
    }
    return true;
  }
  bool operator!=(const VelSetpoint_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct VelSetpoint_

// alias to use template instance with default allocator
using VelSetpoint =
  tutorial_interfaces::msg::VelSetpoint_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__VEL_SETPOINT__STRUCT_HPP_
