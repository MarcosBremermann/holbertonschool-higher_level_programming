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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
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

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
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

        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
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

        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Get the area of the rectangle
        """
        area = self.height * self.width
        self.area = area
        return self.area

    def display(self):
        """
        Function that prints in stdout
        the rectangle using #
        """
        for u in range(self.y):
            print()

        for i in range(self.height):
            for p in range(self.x):
                print(end=" ")
            for o in range(self.width):
                print('#', end="")
            print()
        return self.display

    def update(self, *args, **kwargs):
        """
        Function that assigns the input
        arguments and kwargs into each attribute
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            elif len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """
        Function that returns a specific
        phrase to be done with the values
        of the variables
        """

        id2 = self.id
        x2 = self.x
        y2 = self.y
        width2 = self.width
        height2 = self.height
        return (f"[Rectangle] ({id2}) {x2}/{y2} - {width2}/{height2}")

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }
