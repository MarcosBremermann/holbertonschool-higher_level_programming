#!/usr/bin/python3
from .base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if width <= 0:
            raise ValueError('Width must be a positive number')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if height <= 0:
            raise ValueError('Height must be a positive number')
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if x <= 0:
            raise ValueError('x must be a positive number')
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if y <= 0:
            raise ValueError('y must be a positive number')
        else:
            self.__y = value
