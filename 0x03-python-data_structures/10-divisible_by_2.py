#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult_lst = []
    for num in my_list:
        if (num % 2 == 0):
            mult_lst.append(True)
        else:
            mult_lst.append(False)
    return (mult_lst)
