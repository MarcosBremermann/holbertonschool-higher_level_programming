#!/usr/bin/python3
"""
square.py - defines class
Square for it's different uses in the project
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    Class level attribute that inherits values
    from Rectangle and privates attributes through
    getter and setter
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the square class
        """

        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """
        Function that returns a specific
        phrase to be done with the values
        of the variables
        """

        return f"[Square] (<{self.id}>) <{self.x}>/<{self.y}> - <{self.width}>"
