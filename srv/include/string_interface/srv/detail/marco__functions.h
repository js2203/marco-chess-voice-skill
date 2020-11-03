// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from string_interface:srv\MARCO.idl
// generated code does not contain a copyright notice

#ifndef STRING_INTERFACE__SRV__DETAIL__MARCO__FUNCTIONS_H_
#define STRING_INTERFACE__SRV__DETAIL__MARCO__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "string_interface/msg/rosidl_generator_c__visibility_control.h"

#include "string_interface/srv/detail/marco__struct.h"

/// Initialize srv/MARCO message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * string_interface__srv__MARCO_Request
 * )) before or use
 * string_interface__srv__MARCO_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
bool
string_interface__srv__MARCO_Request__init(string_interface__srv__MARCO_Request * msg);

/// Finalize srv/MARCO message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
void
string_interface__srv__MARCO_Request__fini(string_interface__srv__MARCO_Request * msg);

/// Create srv/MARCO message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * string_interface__srv__MARCO_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
string_interface__srv__MARCO_Request *
string_interface__srv__MARCO_Request__create();

/// Destroy srv/MARCO message.
/**
 * It calls
 * string_interface__srv__MARCO_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
void
string_interface__srv__MARCO_Request__destroy(string_interface__srv__MARCO_Request * msg);


/// Initialize array of srv/MARCO messages.
/**
 * It allocates the memory for the number of elements and calls
 * string_interface__srv__MARCO_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
bool
string_interface__srv__MARCO_Request__Sequence__init(string_interface__srv__MARCO_Request__Sequence * array, size_t size);

/// Finalize array of srv/MARCO messages.
/**
 * It calls
 * string_interface__srv__MARCO_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
void
string_interface__srv__MARCO_Request__Sequence__fini(string_interface__srv__MARCO_Request__Sequence * array);

/// Create array of srv/MARCO messages.
/**
 * It allocates the memory for the array and calls
 * string_interface__srv__MARCO_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
string_interface__srv__MARCO_Request__Sequence *
string_interface__srv__MARCO_Request__Sequence__create(size_t size);

/// Destroy array of srv/MARCO messages.
/**
 * It calls
 * string_interface__srv__MARCO_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
void
string_interface__srv__MARCO_Request__Sequence__destroy(string_interface__srv__MARCO_Request__Sequence * array);

/// Initialize srv/MARCO message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * string_interface__srv__MARCO_Response
 * )) before or use
 * string_interface__srv__MARCO_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
bool
string_interface__srv__MARCO_Response__init(string_interface__srv__MARCO_Response * msg);

/// Finalize srv/MARCO message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
void
string_interface__srv__MARCO_Response__fini(string_interface__srv__MARCO_Response * msg);

/// Create srv/MARCO message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * string_interface__srv__MARCO_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
string_interface__srv__MARCO_Response *
string_interface__srv__MARCO_Response__create();

/// Destroy srv/MARCO message.
/**
 * It calls
 * string_interface__srv__MARCO_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
void
string_interface__srv__MARCO_Response__destroy(string_interface__srv__MARCO_Response * msg);


/// Initialize array of srv/MARCO messages.
/**
 * It allocates the memory for the number of elements and calls
 * string_interface__srv__MARCO_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
bool
string_interface__srv__MARCO_Response__Sequence__init(string_interface__srv__MARCO_Response__Sequence * array, size_t size);

/// Finalize array of srv/MARCO messages.
/**
 * It calls
 * string_interface__srv__MARCO_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
void
string_interface__srv__MARCO_Response__Sequence__fini(string_interface__srv__MARCO_Response__Sequence * array);

/// Create array of srv/MARCO messages.
/**
 * It allocates the memory for the array and calls
 * string_interface__srv__MARCO_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
string_interface__srv__MARCO_Response__Sequence *
string_interface__srv__MARCO_Response__Sequence__create(size_t size);

/// Destroy array of srv/MARCO messages.
/**
 * It calls
 * string_interface__srv__MARCO_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_string_interface
void
string_interface__srv__MARCO_Response__Sequence__destroy(string_interface__srv__MARCO_Response__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // STRING_INTERFACE__SRV__DETAIL__MARCO__FUNCTIONS_H_
