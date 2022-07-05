#!/usr/bin/python3
"""Module for class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""module containing Rectangle class"""


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {:d}/{:d}".format(Rectangle.__name__,
                                       self.__width, self.__height)
