#!/usr/bin/python3
def best_score(a_dictionary):
    largest = None
    largest_value = 0
    if (a_dictionary is None or len(a_dictionary) == 0):
        return (largest)
    else:
        for key in a_dictionary:
            if (a_dictionary[key] > largest_value):
                largest_value = a_dictionary[key]
                largest = key
        return (largest)
