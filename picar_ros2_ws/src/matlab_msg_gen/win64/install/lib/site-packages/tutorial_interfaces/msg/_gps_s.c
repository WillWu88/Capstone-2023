// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from tutorial_interfaces:msg\GPS.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_generator_c/visibility_control.h"
#include "tutorial_interfaces/msg/gps__struct.h"
#include "tutorial_interfaces/msg/gps__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool tutorial_interfaces__msg__gps__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[33];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp(
        "tutorial_interfaces.msg._gps.GPS",
        full_classname_dest, 32) == 0);
  }
  tutorial_interfaces__msg__GPS * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // latdeg
    PyObject * field = PyObject_GetAttrString(_pymsg, "latdeg");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->latdeg = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // longdeg
    PyObject * field = PyObject_GetAttrString(_pymsg, "longdeg");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->longdeg = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // latmin
    PyObject * field = PyObject_GetAttrString(_pymsg, "latmin");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->latmin = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // longmin
    PyObject * field = PyObject_GetAttrString(_pymsg, "longmin");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->longmin = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // flag
    PyObject * field = PyObject_GetAttrString(_pymsg, "flag");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->flag = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * tutorial_interfaces__msg__gps__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of GPS */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("tutorial_interfaces.msg._gps");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "GPS");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  tutorial_interfaces__msg__GPS * ros_message = (tutorial_interfaces__msg__GPS *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // latdeg
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->latdeg);
    {
      int rc = PyObject_SetAttrString(_pymessage, "latdeg", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // longdeg
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->longdeg);
    {
      int rc = PyObject_SetAttrString(_pymessage, "longdeg", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // latmin
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->latmin);
    {
      int rc = PyObject_SetAttrString(_pymessage, "latmin", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // longmin
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->longmin);
    {
      int rc = PyObject_SetAttrString(_pymessage, "longmin", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // flag
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->flag ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "flag", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
