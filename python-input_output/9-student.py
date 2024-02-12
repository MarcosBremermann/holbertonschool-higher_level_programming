#!/usr/bin/python3
"""
File for write file
"""


class Student:
    """
    class that defines a student by
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        serialized_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (str, int)):
                serialized_dict[key] = value
        return serialized_dict
