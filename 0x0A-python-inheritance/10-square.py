#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle

"""module for square class"""


class Square(Rectangle):
    """class representation of a square"""

    def __init__(self, size):
        """initialisation of the square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """computes the are of the square"""
        return self.__size * self.__size
