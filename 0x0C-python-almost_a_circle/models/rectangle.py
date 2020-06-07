#!/usr/bin/python3
"""rectangle:
        classes:
            Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle:
            __init__: constructor
        """
    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__: constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width: get width"""
        return self.__width

    @width.setter
    def width(self, w):
        """width: set width"""
        self.__width = w

    @property
    def height(self):
        """height: get height"""
        return self.__height

    @height.setter
    def height(self, h):
        """height: set height"""
        self.__height = h

    @property
    def x(self):
        """x: get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """x: set x"""
        self.__x = x

    @property
    def y(self):
        """y: get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """y: set y"""
        self.__y = y
