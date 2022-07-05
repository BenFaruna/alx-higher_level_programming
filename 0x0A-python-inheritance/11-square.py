#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle

"""module for square class"""


class Square(Rectangle):
    """class representation of a square"""

    def __init__(self, size):
        """initialisation of square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[{}] {:d}/{:d}".format(Square.__name__,
                                       self.__size, self.__size)

    def area(self):
        """computes the area of a square"""
        return self.__size * self.__size
