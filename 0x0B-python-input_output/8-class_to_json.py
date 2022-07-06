#!/usr/bin/python3
"""module that gives dictonary description of simple data striucture"""


def class_to_json(obj):
    """returns dictionary description of simple data structue"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
