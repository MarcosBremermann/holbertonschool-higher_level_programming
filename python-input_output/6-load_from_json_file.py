#!/usr/bin/python3
"""
File for write file
"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    """
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
