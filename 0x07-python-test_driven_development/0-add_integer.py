#!/usr/bin/python3
"""
0-add_integer
    functions : add_integer
"""


def add_integer(a, b=98):
    """
    add_integer: add a & b
    @a: first arg
    @b: second arg
    Return: a + b
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
        return

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
        return

    a, b = int(a), int(b)

    return a + b
