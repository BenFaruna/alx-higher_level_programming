#!/usr/bin/python3

def check_int(num):
    return type(num) == int or type(num) == float

def add_integer(a, b=98):
    if not check_int(a):
        raise TypeError("a must be an integer")
    elif not check_int(b):
        raise TypeError("b must be an integer")

    if (type(a) == float or type(b) == float):
        a = int(a)
        b = int(b)

    return (a + b)
