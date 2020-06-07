#!/usr/bin/python3
"""base:
    classes:
        Base
    """


class Base:
    """Base class:
            __init__
        """
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__: constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
