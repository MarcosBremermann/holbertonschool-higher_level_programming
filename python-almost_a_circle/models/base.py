#!/usr/bin/python3
"""
File for the base Class
"""


class Base:
    """
    class that will be the base of
    all the other classes in the project.
    Manages the id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
