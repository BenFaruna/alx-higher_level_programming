#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        col_len = len(row)
        count = 0
        for col in row:
            if count != (col_len - 1):
                print("{:d} ".format(col), end="")
            else:
                print("{:d}".format(col))
            count = count + 1
