#!/usr/bin/python3
"""module for working with JSON"""
import json


def from_json_string(my_str):
    """returns an object represented as a JSON string"""
    return json.loads(my_str)
