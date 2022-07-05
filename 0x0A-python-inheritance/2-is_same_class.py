#!/usr/bin/python3

"""module that checks if two objects are exactly the same class"""


def is_same_class(obj, a_class):
    """function to check if objects is the exactly the same class as a_class"""
    return type(obj) is a_class
