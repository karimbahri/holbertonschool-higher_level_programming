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

    def update(self, *args, **kwargs):
        """update attributes"""
        i = 0
        if len(args):
            for item in args:
                if i == 0:
                    self.id = item
                elif i == 1:
                    self.size = item
                elif i == 2:
                    self.x = item
                elif i == 3:
                    self.y = item
                i += 1

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
