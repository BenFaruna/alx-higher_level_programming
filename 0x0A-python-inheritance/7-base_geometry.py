#!/usr/bin/python3

"""Base geometry module containing methods"""


class BaseGeometry:
    """Empty class for BaseGeometry"""
    def __init__(self):
        """new instance of BaseGeometry"""
        pass

    def area(self):
        """Raises an exception for unimplemented method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
