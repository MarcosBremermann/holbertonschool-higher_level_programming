#!/usr/bin/python3
"""
File with the print_square function
"""


def print_square(size):
    """
    Print a square with the character #.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
