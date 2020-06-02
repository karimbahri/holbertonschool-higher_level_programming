#!/usr/bin/python3
"""
3-is_kind_of_class:
    functions:
        is_king_of_class
"""


def is_kind_of_class(obj, a_class):
    """check is obj is an instance of a_class or that inherited from"""
    return issubclass(type(obj), a_class)
