#!/usr/bin/python3

"""
2-matrix_divided: divide list
    Functions : matrix_divided
"""


def matrix_divided(matrix, div):
    """
    matrix_divided: divide each element of the list
    @a: first integer
    @b: second integer
    Return: list_div
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
        return

    if div == 0:
        raise ZeroDivisionError("division by zero")
        return

    if type(matrix) != list or not matrix or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        return

    list_div = []

    if type(matrix[0]) is list:
        size_row = len(matrix[0])
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            return
        row_div = []
        for col in row:
            if type(col) != int and type(col) != float:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
                return

            if len(row) != size_row:
                raise TypeError("Each row of the matrix must have\
 the same size")
                return

            row_div.append(round((col / div), 2))
        list_div.append(row_div)

    return list_div
