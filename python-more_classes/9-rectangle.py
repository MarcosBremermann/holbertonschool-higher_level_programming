#!/usr/bin/python3
"""
File for class Rectangle
"""


class Rectangle:
    """
    Class representing a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

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
        return 2 * (self.__width + self.__height) if self.__width > 0 and self.__height > 0 else 0

    def __str__(self):
        """
        String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Representation of the rectangle for recreation using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor to print a message when an instance is deleted and decrement the number_of_instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method to return the rectangle with the bigger or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        return rect_1 if area_1 >= area_2 else rect_2 if area_2 > area_1 else rect_1

    @classmethod
    def square(cls, size=0):
        """
        Class method to create a square with equal width and height.
        """
        return cls(width=size, height=size)
