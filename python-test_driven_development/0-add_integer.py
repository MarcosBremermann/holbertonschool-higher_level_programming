#!/usr/bin/python3
"""
Function add_integer
"""


def add_integer(a, b=98):
    """
    function that adds 2 integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    elif a == type(float) or b == type(float):
        a = int(a)
        b = int(b)
        return a + b

    else:
        return a + b
