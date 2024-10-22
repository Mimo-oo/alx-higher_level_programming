#!/usr/bin/python3

"""
A class square that inherits from
rectangle 
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes the class square
        """

        super().__init__(size, size, x=0, y=0, id=None)

    @property
    def size(self):
        """
        Returns the size of a square
        """
        return self.width

    @size.setter(self, value):
        self.width = value
        self.height = value



