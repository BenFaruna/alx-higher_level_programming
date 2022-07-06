#!/usr/bin/python3
"""module for parsing JSON into a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object into a text file, using a json representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f, sort_keys=True)
