#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for line in matrix:
            for column in line:
                print("{:d}".format(column), end=" ")
            print("$")
