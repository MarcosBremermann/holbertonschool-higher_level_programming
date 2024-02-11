#!/usr/bin/python3
"""
File for def is_same_class
"""


def is_same_class(obj, a_class):
    """
    def that returns True if the object is exactly
    an instance of the specified class ; otherwise False.
    """
    return type(obj) is a_class
