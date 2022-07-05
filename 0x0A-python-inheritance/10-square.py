#!/usr/bin/python3
"""module for square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class representation of a square"""

    def __init__(self, size):
        """new instance of Rectangle

        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """computes the are of the square"""
        return self.__size * self.__size
