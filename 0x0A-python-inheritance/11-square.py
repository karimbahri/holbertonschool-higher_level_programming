#!/usr/bin/python3
"""
10-square:
    classes:
        Square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square: inherits from rectangle"""
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        str: string representation of the object
        """
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
