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
        """
        Initialization of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            with open(list_dictionaries, "r", encoding"utf-8") as f:
                to_json = f.dumps(list_dictionaries)
            return to_json
