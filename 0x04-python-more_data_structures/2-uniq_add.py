#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    used = []
    for ele in my_list:
        if (ele not in used):
            total += ele
            used.append(ele)

    return (total)
