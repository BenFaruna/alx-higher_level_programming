#!/usr/bin/python3
"""module for working with JSON"""
import json


def to_json_string(my_obj):
    """returns JSOM representation of a string"""
    return json.dumps(my_obj, sort_keys=True)
