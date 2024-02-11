#!/usr/bin/python3
"""
File for class Rectangle
"""


class Rectangle:
    """
    Class representing a rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializer
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Property to retrieve width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set width.
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
        Property to retrieve height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method to set height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Public instance method to calculate the rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method to calculate the rectangle perimeter.
        """
        return 2 * (self.__width + self.__height) \
            if self.__width > 0 and self.__height > 0 else 0

    def __str__(self):
        """
        String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return \
                "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Representation of the rectangle for recreation using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor to print a message when instance is delet
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
