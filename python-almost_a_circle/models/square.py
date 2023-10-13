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

    @property
    def size(self):
        """
        Get the size of the Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the Square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Function that assigns the input
        arguments and kwargs into each attribute
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.x = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)
