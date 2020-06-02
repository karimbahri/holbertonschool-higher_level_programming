#!/usr/bin/python3
"""
    0-lookup:
        functions:
            * lookup
"""


def lookup(obj):
    """
    lookup: return list of attributes and methods of the object
    """
    ls = dir(obj)
    return ls
