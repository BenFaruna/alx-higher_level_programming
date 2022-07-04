#!/usr/bin/python3

"""
Define a rectangle class
"""


class Rectangle:
    """Representation of a rectangle, using width and
    height for initialization"""

    def __init__(self, width=0, height=0):
        """initializes the Rectangle"""
        self.width = width
        self.height = height

    def check_val(name, val):
        """Checkes the values passed as width and height to ensure
        it is a real number"""
        if (type(val) != int):
            raise TypeError("{} must be an integer".format(name))
        elif (val < 0):
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """getter function for private instance of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter function for private instance of width"""
        Rectangle.check_val("width", width)
        self.__width = width

    @property
    def height(self):
        """getter function for private instance of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """getter function for private instance of heigth"""
        Rectangle.check_val("height", height)
        self.__height = height
