#!/usr/bin/python3
"""module that have function to read text file"""


def read_file(filename=""):
    """function to read and print file content"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
