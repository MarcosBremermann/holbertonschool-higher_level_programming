#!/usr/bin/python3
"""
base.py - Defines the Base class, the foundation\
for all other classes in the project.
"""
import json


class Base:
    """
    Class-level attribute to keep track of\
    the number of instances created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Function that returns dictionary in
        JSON style
        """
        if list_dictionaries is None:
            return "[]"
        else:
            json_dict = json.dumps(list_dictionaries)
            return json_dict
