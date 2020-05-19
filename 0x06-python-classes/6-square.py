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
    def __init__(self, size=0, position=(0, 0)):
        """documentation of the method __init__: constructor"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not check_pos(position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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

    @property
    def position(self):
        """the documentation of the method position: position"""
        return self.__position

    @position.setter
    def position(self, value):
        """documentation of the method position: check for position"""
        if not check_pos(position):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """documentation of the methode my_print"""
        if not self.__size:
            print("")
            return
        for l in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end='')
            print("")


def check_pos(position):
    """documentation of check_pos : check position is valid"""
    if type(position) != tuple or len(position) != 2:
        return False
    if type(position[0]) != int or type(position[1]) != int:
        return False
    if position[0] < 0 or position[1] < 0:
        return False
    return True
