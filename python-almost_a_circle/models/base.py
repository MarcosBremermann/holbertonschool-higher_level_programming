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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function that saves
        list into .json format
        """
        file = cls.__name__ + ".json"
        temp = []
        if list_objs:
            for i in list_objs:
                temp.append(i.to_dictionary())
        with open(file, "w") as f:
            f.write(Base.to_json_string(temp))

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list
        of the JSON string representation
        """
        if json_string is None or json_string == '[]':
            return []
        tempo = json.loads(json_string)
        return tempo

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that that returns an instance with
        all attributes already set
        """
        dummy = 0
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
