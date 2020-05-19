#!/usr/bin/python3
"""
    documentation of the module square
        *Classes:
            1 - Square
"""


class Square:
    """
    documentation of the class Square
        *methodes:
            __init__
        *attributes:
            size: private
    """
    def __init__(self, size=0):
        """documentation of the method __init__ : constructor"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
