#!/usr/bin/python3
"""module for writing string into a file"""


def write_file(filename="", text=""):
    """function that writes string to file"""
    with open(filename, "w", encoding="utf-8") as f:
        str_len = f.write(text)
    return str_len
