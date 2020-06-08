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
        check_int(w, "width must be an integer")
        check_strictly_positive(w, "width")
        self.__width = w

    @property
    def height(self):
        """height: get height"""
        return self.__height

    @height.setter
    def height(self, h):
        """height: set height"""
        check_int(h, "height must be an integer")
        check_strictly_positive(h, "height")
        self.__height = h

    @property
    def x(self):
        """x: get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """x: set x"""
        check_int(x, "x must be an integer")
        check_positive(x, "x")
        self.__x = x

    @property
    def y(self):
        """y: get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """y: set y"""
        check_int(y, "y must be an integer")
        check_positive(y, "y")
        self.__y = y

    def area(self):
        """return the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """print a rectangle"""
        for i in range(self.__y):
            print("")
        for h in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """print string representation of rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update attributes"""
        i = 0
        if len(args):
            for item in args:
                if i == 0:
                    self.id = item
                elif i == 1:
                    self.__width = item
                elif i == 2:
                    self.__height = item
                elif i == 3:
                    self.__x = item
                elif i == 4:
                    self.__y = item
                i += 1

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


def check_int(value, log):
    """check_int: check if value is int"""
    if type(value) is not int:
        raise TypeError(log)


def check_positive(value, valueName):
    """check if value is positive of equal to 0"""
    if value < 0:
        raise ValueError("{} must be >= 0".format(valueName))


def check_strictly_positive(value, valueName):
    """check if value is strictly_positive"""
    if value <= 0:
        raise ValueError("{} must be > 0".format(valueName))
