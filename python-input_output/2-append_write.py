#!/usr/bin/python3
"""
File for write file
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """

    try:
        with open(filename, 'a', encoding='utf-8') as file:
            char_count = file.write(text)
            return char_count
    except Exception as e:
        print(f"Error: {e}")
        return 0
