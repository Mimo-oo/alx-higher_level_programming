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

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updating the square
        """
        if args and len(args) != 0:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                else:
                    continue

        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = valiue

    def to_dictionary(self):
        """
       Return dictionary representation of a square
        """
        square_dict = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }

        return square_dict
