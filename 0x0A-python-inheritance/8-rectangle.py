#!/usr/bin/python3
"""Module for class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""module containing Rectangle class"""


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """initialise the Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
