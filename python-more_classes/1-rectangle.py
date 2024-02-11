#!/usr/bin/python3
"""
File for class Rectangle
"""

class Rectangle:
    """
    Class representing a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializer
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        property to retrieve width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        def to set width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        property to retrieve height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        def to set height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
