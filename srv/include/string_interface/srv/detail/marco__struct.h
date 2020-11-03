// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from string_interface:srv\MARCO.idl
// generated code does not contain a copyright notice

#ifndef STRING_INTERFACE__SRV__DETAIL__MARCO__STRUCT_H_
#define STRING_INTERFACE__SRV__DETAIL__MARCO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'req'
#include "rosidl_runtime_c/string.h"

// Struct defined in srv/MARCO in the package string_interface.
typedef struct string_interface__srv__MARCO_Request
{
  rosidl_runtime_c__String req;
} string_interface__srv__MARCO_Request;

// Struct for a sequence of string_interface__srv__MARCO_Request.
typedef struct string_interface__srv__MARCO_Request__Sequence
{
  string_interface__srv__MARCO_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} string_interface__srv__MARCO_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'res'
// already included above
// #include "rosidl_runtime_c/string.h"

// Struct defined in srv/MARCO in the package string_interface.
typedef struct string_interface__srv__MARCO_Response
{
  rosidl_runtime_c__String res;
} string_interface__srv__MARCO_Response;

// Struct for a sequence of string_interface__srv__MARCO_Response.
typedef struct string_interface__srv__MARCO_Response__Sequence
{
  string_interface__srv__MARCO_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} string_interface__srv__MARCO_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // STRING_INTERFACE__SRV__DETAIL__MARCO__STRUCT_H_
