#!/usr/bin/python3
"""module for working with file"""


def append_write(filename="", text=""):
    """function that appends text to the end of a file"""
    with open(filename, "a", encoding="utf-8") as f:
        str_len = f.write(text)
    return str_len
