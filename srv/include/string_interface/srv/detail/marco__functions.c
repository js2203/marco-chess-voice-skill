// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from string_interface:srv\MARCO.idl
// generated code does not contain a copyright notice
#include "string_interface/srv/detail/marco__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// Include directives for member types
// Member `req`
#include "rosidl_runtime_c/string_functions.h"

bool
string_interface__srv__MARCO_Request__init(string_interface__srv__MARCO_Request * msg)
{
  if (!msg) {
    return false;
  }
  // req
  if (!rosidl_runtime_c__String__init(&msg->req)) {
    string_interface__srv__MARCO_Request__fini(msg);
    return false;
  }
  return true;
}

void
string_interface__srv__MARCO_Request__fini(string_interface__srv__MARCO_Request * msg)
{
  if (!msg) {
    return;
  }
  // req
  rosidl_runtime_c__String__fini(&msg->req);
}

string_interface__srv__MARCO_Request *
string_interface__srv__MARCO_Request__create()
{
  string_interface__srv__MARCO_Request * msg = (string_interface__srv__MARCO_Request *)malloc(sizeof(string_interface__srv__MARCO_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(string_interface__srv__MARCO_Request));
  bool success = string_interface__srv__MARCO_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
string_interface__srv__MARCO_Request__destroy(string_interface__srv__MARCO_Request * msg)
{
  if (msg) {
    string_interface__srv__MARCO_Request__fini(msg);
  }
  free(msg);
}


bool
string_interface__srv__MARCO_Request__Sequence__init(string_interface__srv__MARCO_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  string_interface__srv__MARCO_Request * data = NULL;
  if (size) {
    data = (string_interface__srv__MARCO_Request *)calloc(size, sizeof(string_interface__srv__MARCO_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = string_interface__srv__MARCO_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        string_interface__srv__MARCO_Request__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
string_interface__srv__MARCO_Request__Sequence__fini(string_interface__srv__MARCO_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      string_interface__srv__MARCO_Request__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

string_interface__srv__MARCO_Request__Sequence *
string_interface__srv__MARCO_Request__Sequence__create(size_t size)
{
  string_interface__srv__MARCO_Request__Sequence * array = (string_interface__srv__MARCO_Request__Sequence *)malloc(sizeof(string_interface__srv__MARCO_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = string_interface__srv__MARCO_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
string_interface__srv__MARCO_Request__Sequence__destroy(string_interface__srv__MARCO_Request__Sequence * array)
{
  if (array) {
    string_interface__srv__MARCO_Request__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `res`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
string_interface__srv__MARCO_Response__init(string_interface__srv__MARCO_Response * msg)
{
  if (!msg) {
    return false;
  }
  // res
  if (!rosidl_runtime_c__String__init(&msg->res)) {
    string_interface__srv__MARCO_Response__fini(msg);
    return false;
  }
  return true;
}

void
string_interface__srv__MARCO_Response__fini(string_interface__srv__MARCO_Response * msg)
{
  if (!msg) {
    return;
  }
  // res
  rosidl_runtime_c__String__fini(&msg->res);
}

string_interface__srv__MARCO_Response *
string_interface__srv__MARCO_Response__create()
{
  string_interface__srv__MARCO_Response * msg = (string_interface__srv__MARCO_Response *)malloc(sizeof(string_interface__srv__MARCO_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(string_interface__srv__MARCO_Response));
  bool success = string_interface__srv__MARCO_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
string_interface__srv__MARCO_Response__destroy(string_interface__srv__MARCO_Response * msg)
{
  if (msg) {
    string_interface__srv__MARCO_Response__fini(msg);
  }
  free(msg);
}


bool
string_interface__srv__MARCO_Response__Sequence__init(string_interface__srv__MARCO_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  string_interface__srv__MARCO_Response * data = NULL;
  if (size) {
    data = (string_interface__srv__MARCO_Response *)calloc(size, sizeof(string_interface__srv__MARCO_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = string_interface__srv__MARCO_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        string_interface__srv__MARCO_Response__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
string_interface__srv__MARCO_Response__Sequence__fini(string_interface__srv__MARCO_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      string_interface__srv__MARCO_Response__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

string_interface__srv__MARCO_Response__Sequence *
string_interface__srv__MARCO_Response__Sequence__create(size_t size)
{
  string_interface__srv__MARCO_Response__Sequence * array = (string_interface__srv__MARCO_Response__Sequence *)malloc(sizeof(string_interface__srv__MARCO_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = string_interface__srv__MARCO_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
string_interface__srv__MARCO_Response__Sequence__destroy(string_interface__srv__MARCO_Response__Sequence * array)
{
  if (array) {
    string_interface__srv__MARCO_Response__Sequence__fini(array);
  }
  free(array);
}
