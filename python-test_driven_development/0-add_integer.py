#!/usr/bin/python3
"""
File that writes a function that adds integers
"""
def add_integer(a, b=98):
    """
    Function that adds two numbers if they're both
    either integer or float. In case either of them
    aren't, raises a TypeError
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return a + b
