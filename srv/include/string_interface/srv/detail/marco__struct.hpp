// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from string_interface:srv\MARCO.idl
// generated code does not contain a copyright notice

#ifndef STRING_INTERFACE__SRV__DETAIL__MARCO__STRUCT_HPP_
#define STRING_INTERFACE__SRV__DETAIL__MARCO__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__string_interface__srv__MARCO_Request __attribute__((deprecated))
#else
# define DEPRECATED__string_interface__srv__MARCO_Request __declspec(deprecated)
#endif

namespace string_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MARCO_Request_
{
  using Type = MARCO_Request_<ContainerAllocator>;

  explicit MARCO_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->req = "";
    }
  }

  explicit MARCO_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : req(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->req = "";
    }
  }

  // field types and members
  using _req_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _req_type req;

  // setters for named parameter idiom
  Type & set__req(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->req = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    string_interface::srv::MARCO_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const string_interface::srv::MARCO_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<string_interface::srv::MARCO_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<string_interface::srv::MARCO_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      string_interface::srv::MARCO_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<string_interface::srv::MARCO_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      string_interface::srv::MARCO_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<string_interface::srv::MARCO_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<string_interface::srv::MARCO_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<string_interface::srv::MARCO_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__string_interface__srv__MARCO_Request
    std::shared_ptr<string_interface::srv::MARCO_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__string_interface__srv__MARCO_Request
    std::shared_ptr<string_interface::srv::MARCO_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MARCO_Request_ & other) const
  {
    if (this->req != other.req) {
      return false;
    }
    return true;
  }
  bool operator!=(const MARCO_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MARCO_Request_

// alias to use template instance with default allocator
using MARCO_Request =
  string_interface::srv::MARCO_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace string_interface


#ifndef _WIN32
# define DEPRECATED__string_interface__srv__MARCO_Response __attribute__((deprecated))
#else
# define DEPRECATED__string_interface__srv__MARCO_Response __declspec(deprecated)
#endif

namespace string_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MARCO_Response_
{
  using Type = MARCO_Response_<ContainerAllocator>;

  explicit MARCO_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->res = "";
    }
  }

  explicit MARCO_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : res(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->res = "";
    }
  }

  // field types and members
  using _res_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _res_type res;

  // setters for named parameter idiom
  Type & set__res(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->res = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    string_interface::srv::MARCO_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const string_interface::srv::MARCO_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<string_interface::srv::MARCO_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<string_interface::srv::MARCO_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      string_interface::srv::MARCO_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<string_interface::srv::MARCO_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      string_interface::srv::MARCO_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<string_interface::srv::MARCO_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<string_interface::srv::MARCO_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<string_interface::srv::MARCO_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__string_interface__srv__MARCO_Response
    std::shared_ptr<string_interface::srv::MARCO_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__string_interface__srv__MARCO_Response
    std::shared_ptr<string_interface::srv::MARCO_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MARCO_Response_ & other) const
  {
    if (this->res != other.res) {
      return false;
    }
    return true;
  }
  bool operator!=(const MARCO_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MARCO_Response_

// alias to use template instance with default allocator
using MARCO_Response =
  string_interface::srv::MARCO_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace string_interface

namespace string_interface
{

namespace srv
{

struct MARCO
{
  using Request = string_interface::srv::MARCO_Request;
  using Response = string_interface::srv::MARCO_Response;
};

}  // namespace srv

}  // namespace string_interface

#endif  // STRING_INTERFACE__SRV__DETAIL__MARCO__STRUCT_HPP_
