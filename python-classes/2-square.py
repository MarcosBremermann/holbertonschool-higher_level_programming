#!/usr/bin/python3
"""
File that defines a class Square
"""


class Square:
    """
    class Square
    """

    def __init__(self, size=0):
        """
        This is a initialiation process that
        defines size as a private instance attribute
        checks if size is not an integer nor that
        it is less than zero, raising errors in
        both of those cases
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
