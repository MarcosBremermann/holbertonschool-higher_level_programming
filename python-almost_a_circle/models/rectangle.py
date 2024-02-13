#!/usr/bin/python3
"""
File for the rectangle Class
"""
from .base import Base


class Rectangle(Base):
    """
    class Rectangle that gets and sets its own atr.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class Constructor
        """
        super(). __init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        public setter for width
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be greater than zero.")
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        public setter for height
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be greater than zero.")
        else:
            self.__height = value

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        public setter for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be greater than zero")
        else:
            self.__x = value

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        public setter for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be greater than zero")
        else:
            self.__y = value
