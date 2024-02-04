#!/usr/bin/python3
"""
File for class Square
"""


class Square:
    """
    Square Class
    """

    def __init__(self, size=0):
        """
        Initialization for priv. inst. att. size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
