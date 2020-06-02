#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle
"""
10-square:
    classes:
        Square
"""

class Square(Rectangle):
    """Square: inherits from rectangle"""
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
