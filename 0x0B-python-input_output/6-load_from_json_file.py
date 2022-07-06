#!/usr/bin/python3
"""module for working with JSON and file"""
import json


def load_from_json_file(filename):
    """function that creates object from a JSON file"""
    with open(filename, "r") as f:
        return json.load(f)
