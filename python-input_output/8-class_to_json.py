#!/usr/bin/python3
"""
File for write file
"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data structure
    """

    if not hasattr(obj, '__dict__'):
        raise ValueError("Input object is not an instance of a class.")

    serialized_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_dict[key] = value
    return serialized_dict
