# generated from rosidl_generator_py/resource/_idl.py.em
# with input from tutorial_interfaces:msg/GPS.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GPS(type):
    """Metaclass of message 'GPS'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('tutorial_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'tutorial_interfaces.msg.GPS')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__gps
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__gps
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__gps
            cls._TYPE_SUPPORT = module.type_support_msg__msg__gps
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__gps

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GPS(metaclass=Metaclass_GPS):
    """Message class 'GPS'."""

    __slots__ = [
        '_header',
        '_latitude_degrees',
        '_longitude_degrees',
        '_latitude_minutes',
        '_longitude_minutes',
        '_flag',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'latitude_degrees': 'double',
        'longitude_degrees': 'double',
        'latitude_minutes': 'double',
        'longitude_minutes': 'double',
        'flag': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.latitude_degrees = kwargs.get('latitude_degrees', float())
        self.longitude_degrees = kwargs.get('longitude_degrees', float())
        self.latitude_minutes = kwargs.get('latitude_minutes', float())
        self.longitude_minutes = kwargs.get('longitude_minutes', float())
        self.flag = kwargs.get('flag', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.latitude_degrees != other.latitude_degrees:
            return False
        if self.longitude_degrees != other.longitude_degrees:
            return False
        if self.latitude_minutes != other.latitude_minutes:
            return False
        if self.longitude_minutes != other.longitude_minutes:
            return False
        if self.flag != other.flag:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def latitude_degrees(self):
        """Message field 'latitude_degrees'."""
        return self._latitude_degrees

    @latitude_degrees.setter
    def latitude_degrees(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'latitude_degrees' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'latitude_degrees' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._latitude_degrees = value

    @builtins.property
    def longitude_degrees(self):
        """Message field 'longitude_degrees'."""
        return self._longitude_degrees

    @longitude_degrees.setter
    def longitude_degrees(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'longitude_degrees' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'longitude_degrees' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._longitude_degrees = value

    @builtins.property
    def latitude_minutes(self):
        """Message field 'latitude_minutes'."""
        return self._latitude_minutes

    @latitude_minutes.setter
    def latitude_minutes(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'latitude_minutes' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'latitude_minutes' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._latitude_minutes = value

    @builtins.property
    def longitude_minutes(self):
        """Message field 'longitude_minutes'."""
        return self._longitude_minutes

    @longitude_minutes.setter
    def longitude_minutes(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'longitude_minutes' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'longitude_minutes' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._longitude_minutes = value

    @builtins.property
    def flag(self):
        """Message field 'flag'."""
        return self._flag

    @flag.setter
    def flag(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'flag' field must be of type 'bool'"
        self._flag = value
