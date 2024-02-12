#!/usr/bin/python3
"""
File for read file
"""


def read_file(filename=""):
    """
    file that reads and prints in stdout
    """

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error: {e}")
