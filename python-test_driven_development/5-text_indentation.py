#!/usr/bin/python3
"""
File with the text_indentation function
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after '.', '?', and ':'.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""

    for char in text:
        line += char

        if char in ['.', '?', ':']:
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip())