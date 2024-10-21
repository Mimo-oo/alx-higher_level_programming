#!/usr/bin/python3
"""
This is a class that inherit from thee class Base
"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):

        """Initialize a new Rectangle.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(self, id=None)

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter
        """
        self.__width = width

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """

        self.__height = value

    @property
    def x(self):
        """
        x getter
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """

        self.__x = value

    @property
    def y(self):
        """
        y getter
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """

        self.__y = value

