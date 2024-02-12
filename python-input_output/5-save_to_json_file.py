#!/usr/bin/python3
"""
File for write file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """

    try:
        with open(filename, 'w') as file:
            json.dump(my_obj, file)
    except Exception as e:
        print(f"Error: {e}")
