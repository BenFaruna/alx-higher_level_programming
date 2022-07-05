#!/usr/bin/python3

"""module for class of MyList extending the list data structure"""


class MyList(list):
    """Class that inherits from inbuilt list"""

    def print_sorted(self):
        """method that prints list in sorted manner"""
        print(sorted(self))
