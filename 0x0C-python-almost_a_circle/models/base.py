#!/usr/bin/python3

"""
Defines a base model class.
"""


class Base:

    """
    Represents the base model
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = int(id)

        else:
            __nb_objects += 1
            self.id = __nb_objects
