#!/usr/bin/python3
"Defines a class Square"


class Square:
    """Class Square that defines a square:
    -Private instance attribute: size
    -Instantiation with size (no type/value verification)"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        return False

    def __ne__(self, other):
        if self.area() != other.area():
            return True
        return False

    def __lt__(self, other):
        if self.area() < other.area():
            return True
        return False

    def __le__(self, other):
        if self.area() <= other.area():
            return True
        return False

    def __gt__(self, other):
        if self.area() > other.area():
            return True
        return False

    def __ge__(self, other):
        if self.area() >= other.area():
            return True
        return False