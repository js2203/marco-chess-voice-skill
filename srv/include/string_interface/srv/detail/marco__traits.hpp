// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from string_interface:srv\MARCO.idl
// generated code does not contain a copyright notice

#ifndef STRING_INTERFACE__SRV__DETAIL__MARCO__TRAITS_HPP_
#define STRING_INTERFACE__SRV__DETAIL__MARCO__TRAITS_HPP_

#include "string_interface/srv/detail/marco__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<string_interface::srv::MARCO_Request>()
{
  return "string_interface::srv::MARCO_Request";
}

template<>
inline const char * name<string_interface::srv::MARCO_Request>()
{
  return "string_interface/srv/MARCO_Request";
}

template<>
struct has_fixed_size<string_interface::srv::MARCO_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<string_interface::srv::MARCO_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<string_interface::srv::MARCO_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<string_interface::srv::MARCO_Response>()
{
  return "string_interface::srv::MARCO_Response";
}

template<>
inline const char * name<string_interface::srv::MARCO_Response>()
{
  return "string_interface/srv/MARCO_Response";
}

template<>
struct has_fixed_size<string_interface::srv::MARCO_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<string_interface::srv::MARCO_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<string_interface::srv::MARCO_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<string_interface::srv::MARCO>()
{
  return "string_interface::srv::MARCO";
}

template<>
inline const char * name<string_interface::srv::MARCO>()
{
  return "string_interface/srv/MARCO";
}

template<>
struct has_fixed_size<string_interface::srv::MARCO>
  : std::integral_constant<
    bool,
    has_fixed_size<string_interface::srv::MARCO_Request>::value &&
    has_fixed_size<string_interface::srv::MARCO_Response>::value
  >
{
};

template<>
struct has_bounded_size<string_interface::srv::MARCO>
  : std::integral_constant<
    bool,
    has_bounded_size<string_interface::srv::MARCO_Request>::value &&
    has_bounded_size<string_interface::srv::MARCO_Response>::value
  >
{
};

template<>
struct is_service<string_interface::srv::MARCO>
  : std::true_type
{
};

template<>
struct is_service_request<string_interface::srv::MARCO_Request>
  : std::true_type
{
};

template<>
struct is_service_response<string_interface::srv::MARCO_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // STRING_INTERFACE__SRV__DETAIL__MARCO__TRAITS_HPP_
