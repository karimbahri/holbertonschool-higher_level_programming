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
            area
            size
        *attributes:
            size: private
    """
    def __init__(self, size=0):
        """documentation of the method __init__: constructor"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """documentation of the method area: return the area of square"""
        return self.__size**2

    @property
    def size(self):
        """documentation of the method size: getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """documentation of the method size: setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __eq__(self, sqr):
        return self.area() == sqr.area()

    def __ne__(self, sqr):
        return not self == sqr

    def __bg__(self, sqr):
        return self.area() > sqr.area()

    def __le__(self, sqr):
        return not self > sqr

    def __lt__(self, sqr):
        return self.area() < sqr.area()

    def __be__(self, sqr):
        return not self < sqr
