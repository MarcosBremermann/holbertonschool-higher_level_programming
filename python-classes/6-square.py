#!/usr/bin/python3
"""
File for class Square
"""


class Square:
    """
    Square Class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializer
        """

        self.__position = position
        self.__size = size

    @property
    def size(self):
        """
        Getter for priv. inst. att. size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for priv. inst. att. size
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter for priv. inst. att. position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for priv. inst. att. position
        """

        for number in position:
            if number <= 0:
                raise \
                    TypeError("position must be \
                    a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        def that  returns the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        def that prints in stdout the square with the character #
        """
        if self.size == 0:
            print()

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
