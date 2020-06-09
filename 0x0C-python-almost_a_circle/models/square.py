#!/usr/bin/python3
"""square:
        classes:
            square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square: inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """__init__: constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str: string representation of square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, size):
        """set size"""
        self.width = size
        self.height = size
