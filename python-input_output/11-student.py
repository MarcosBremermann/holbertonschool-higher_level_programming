#!/usr/bin/python3
"""
File for write file
"""


class Student:
    """
    class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        serialized_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                serialized_dict[attr] = getattr(self, attr)
        return serialized_dict

    def reload_from_json(self, json_data):
        for key, value in json_data.items():
            setattr(self, key, value)
