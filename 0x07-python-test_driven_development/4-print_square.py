#!/usr/bin/python3
"""
4-print_square:
    Function:
        print_square
"""


def print_square(size):
    """
    print_square
            args:
                @size: size of the square
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
        return

    if size < 0:
        raise ValueError("size must be >= 0")
        return

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
