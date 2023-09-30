#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    z_dictionary = {}

    for key, value in a_dictionary.items():
        z_dictionary[key] = value * 2

    return z_dictionary
