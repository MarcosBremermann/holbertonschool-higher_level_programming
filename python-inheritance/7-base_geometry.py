#!/usr/bin/python3
"""
File for def is_same_class
"""


class BaseGeometry:
    """
    Class with:
    Public instance method: def area(self):
        that raises an Exception with the message area() is not implemented
    Public instance method: def integer_validator(self, name, value):
        that validates value: you can assume name is always a string
    if value is not an integer:
        raise a TypeError exception, with the message <name> must be an integer
    if value is less or equal to 0:
        raise a ValueError with the message <name> must be greater than 0
    """

    def area(self):
        """
        just fpor pycode
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        just for pycode
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
