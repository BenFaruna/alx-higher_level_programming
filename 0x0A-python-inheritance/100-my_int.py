#!/usr/bin/python3

"""class MyInt that is a rebel"""


class MyInt(int):
    """MyInt class with builtin extended for integer"""
    def __init__(self, value):
        self.__value = value

    def __eq__(self, x):
        """equal to inversion"""
        return self.__value != x

    def __ne__(self, x):
        """not equal to inversion"""
        return self.__value == x
