#!/usr/bin/python3
"""
0-rectangle
    Classes:
        * Rectangle
"""


class Rectangle:
    """
    Rectangle:
        methodes:
            * __init__
    """
    def __init__(self, width=0, height=0):
        """__init__: constructor"""
        self.__width = width
        self.__height = height

    def width_get(self):
        """width: retrieve width"""
        return self.__width

    def width_set(self, value):
        """width: set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    width = property(width_get, width_set)

    def height_get(self):
        """height: retrieve the height"""
        return self.__height

    def height_set(self, value):
        """height: set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    height = property(height_get, height_set)

    def area(self):
        """area: return area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter: return the perimeter of the rectangle"""
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        __str__: string representation of the instance
        """
        rect = ""
        if not self.__width or not self.__height:
            return rect
        for i in range(self.__height):
            for j in range(self.__width):
                rect += '#'
            rect += '\n'

        rect = rect[:-1]

        return rect

    def __repr__(self):
        """
        __repr__: string representation of the instance
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        ___del__: destructor
        """
        print("Bye rectangle...")
