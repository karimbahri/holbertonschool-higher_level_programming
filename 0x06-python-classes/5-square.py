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
            my_print
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

    def my_print(self):
        """documentation of the methode my_print"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print("")
