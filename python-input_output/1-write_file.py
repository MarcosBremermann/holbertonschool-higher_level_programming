#!/usr/bin/python3
"""
File for write file
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            char_count = file.write(text)
            return char_count
    except Exception as e:
        print(f"Error: {e}")
        return 0
