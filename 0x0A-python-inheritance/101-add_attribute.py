#!/usr/bin/python3
"""Module to add attribute method"""

def add_attribute(obj, name, value):
    """function for adding new attributes to an object"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
