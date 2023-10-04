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
        Function that initializes size as a
        Private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """
        This is a function that when
        called returns the area of a
        square
        """

        return self.__size ** 2

    @property
    def size(self):
        """
        Function that retrieves the private
        instance attributes from the self
        variable
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Function that checks if size
        is an integer or less than zero,
        in either case raising errors.
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """
        Function that prints the square
        using only '#'
        """

        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
