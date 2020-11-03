// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from string_interface:srv\MARCO.idl
// generated code does not contain a copyright notice

#ifndef STRING_INTERFACE__SRV__DETAIL__MARCO__BUILDER_HPP_
#define STRING_INTERFACE__SRV__DETAIL__MARCO__BUILDER_HPP_

#include "string_interface/srv/detail/marco__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace string_interface
{

namespace srv
{

namespace builder
{

class Init_MARCO_Request_req
{
public:
  Init_MARCO_Request_req()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::string_interface::srv::MARCO_Request req(::string_interface::srv::MARCO_Request::_req_type arg)
  {
    msg_.req = std::move(arg);
    return std::move(msg_);
  }

private:
  ::string_interface::srv::MARCO_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::string_interface::srv::MARCO_Request>()
{
  return string_interface::srv::builder::Init_MARCO_Request_req();
}

}  // namespace string_interface


namespace string_interface
{

namespace srv
{

namespace builder
{

class Init_MARCO_Response_res
{
public:
  Init_MARCO_Response_res()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::string_interface::srv::MARCO_Response res(::string_interface::srv::MARCO_Response::_res_type arg)
  {
    msg_.res = std::move(arg);
    return std::move(msg_);
  }

private:
  ::string_interface::srv::MARCO_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::string_interface::srv::MARCO_Response>()
{
  return string_interface::srv::builder::Init_MARCO_Response_res();
}

}  // namespace string_interface

#endif  // STRING_INTERFACE__SRV__DETAIL__MARCO__BUILDER_HPP_
