#!/usr/bin/python3
"""
File for def lookup
"""


class MyList(list):
    """
    class that sorts and prints list
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
