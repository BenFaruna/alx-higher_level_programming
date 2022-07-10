#!/usr/bin/python3
from .base import Base
"""Module for the rectangle class"""


class Rectangle(Base):
    """rectangle class with private attributes width, height, x, y"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """string representation of the Rectangle class"""
        return "[{}] ({}) {}/{} - {}/{}".format(Rectangle.__name__, self.id,
                                                self.x, self.y, self.width,
                                                self.height)

    def check_int(name, value):
        """function that checks if a value is an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

    def under_zero(name, value):
        """function that checks if a number is greater
        or equal  to zero else it raises an exception"""
        if (value < 0):
            raise ValueError("{} must be >= 0".format(name))

    def under_or_equal_zero(name, value):
        """function that checks if a number is greater than zero
        else it raises an exception"""
        if (value <= 0):
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """helper function for private attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """helper function for width for setting value"""
        Rectangle.check_int("width", width)
        Rectangle.under_or_equal_zero("width", width)
        self.__width = width

    @property
    def height(self):
        """helper function for private attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """helper function for height for setting value"""
        Rectangle.check_int("height", height)
        Rectangle.under_or_equal_zero("height", height)
        self.__height = height

    @property
    def x(self):
        """helper function for private attribute x"""
        return self.__x

    @x.setter
    def x(self, x):
        """helper function for x for setting value"""
        Rectangle.check_int("x", x)
        Rectangle.under_zero("x", x)
        self.__x = x

    @property
    def y(self):
        """helper function for private attribute y"""
        return self.__y

    @y.setter
    def y(self, y):
        """helper function for y for setting value"""
        Rectangle.check_int("y", y)
        Rectangle.under_zero("y", y)
        self.__y = y

    def area(self):
        """function that returns the area of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints the rectangle eith the character #"""
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle class"""
        if len(args) != 0:
            attr_index = 0
            attrs = ["id", "width", "height", "x", "y"]
            for arg in args:
                setattr(self, attrs[attr_index], arg)
                attr_index += 1
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """returns dictionary representation of Rectangle class"""
        attrs = ["x", "y", "id", "height", "width"]
        return {attr: getattr(self, attr) for attr in attrs}
