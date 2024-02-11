#!/usr/bin/python3
"""
File for def lookup
"""


def lookup(obj):
    """
    def that the list of available attributes
    and methods of an object
    """
    return [attr for attr in dir(obj)]
