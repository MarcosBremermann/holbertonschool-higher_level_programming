#!/usr/bin/python3
"""
File that defines a class Square
"""


class Square:
    """
    class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Function that initializes size and position
        as Private instance attributes
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        elif size < 0:
            raise ValueError('size must be >= 0')

        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        else:
            self.__size = size

        for i in position:
            if not isinstance(i, int):
                raise TypeError('position must be a \
                tuple of 2 positive integers')
            elif i < 0:
                raise TypeError('position must be a \
                tuple of 2 positive integers')
        self.__position = position

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
        instance attributes from the size
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
        Prints the square using '#' and position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print('_' * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """
        Function that retrieves the private
        instance attributes from the position
        variable
        """
        return self.__position

    @position.setter
    def position(self, value):
        if len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in position:
            if not isinstance(i, int) or i < 0:
                raise TypeError('position must be a \
                tuple of 2 positive integers')
        self.__position = position
