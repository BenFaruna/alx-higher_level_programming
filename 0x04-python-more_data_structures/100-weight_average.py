#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    if (len(my_list) == 0 or my_list is None):
        return (average)

    denom = sum([i[1] for i in my_list])
    numer = sum([i * j for (i, j) in my_list])
    average = numer / denom
    return (average)
