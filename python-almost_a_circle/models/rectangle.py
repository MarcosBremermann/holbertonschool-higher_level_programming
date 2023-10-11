#!/usr/bin/python3
"""
rectangle.py - Defines the Rectangle class
for other uses in the project
"""
from .base import Base


class Rectangle(Base):
    """
    Class level attribute that inherits values
    from Base and privates attributes through
    getter and setter
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle Class
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Get the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle
        """
        if value <= 0:
            raise ValueError('Width must be a positive number')
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle
        """

        if value <= 0:
            raise ValueError('Height must be a positive number')
        else:
            self.__height = value

    @property
    def x(self):
        """
        Set the x position in the axis of the Rectangle
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Get the x position in the axis of the Rectangle
        """

        if value <= 0:
            raise ValueError('x must be a positive number')
        else:
            self.__x = value

    @property
    def y(self):
        """
        Set the y position in the axis of the Rectangle
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Get the y position in the axis of the Rectangle
        """

        if value <= 0:
            raise ValueError('y must be a positive number')
        else:
            self.__y = value
