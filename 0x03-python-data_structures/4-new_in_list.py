#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = [i for i in my_list]

    if (idx < 0 or idx >= len(my_list)):
        return (None)
    else:
        list_copy[idx] = element
        return (list_copy)
