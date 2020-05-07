#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    pow_matrix = []

    if matrix:
        length = len(matrix)

        for i in range(length):
            line = []
            for j in range(len(matrix[i])):
                line.append(matrix[i][j] ** 2)
            pow_matrix.append(line)
    return pow_matrix
