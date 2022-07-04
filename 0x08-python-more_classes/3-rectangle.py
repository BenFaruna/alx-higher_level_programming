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

    def __str__(self):
        rectangle = ""
        if (self.width == 0 or self.height == 0):
            return ("")
        for height in range(self.height):
            rectangle += ("#" * self.width)
            if (height < self.height - 1):
                rectangle += "\n"
        return rectangle

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

    def perimeter(self):
        """Computes the perimeter of a rectangle"""
        if (self.width == 0 or self.height == 0):
            return (0)
        return (2 * (self.width + self.height))

    def area(self):
        """Computes the area of a rectangle"""
        return (self.width * self.height)
