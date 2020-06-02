#!/usr/bin/python3
"""
add_attribute:
    functions:
        add_attribute
"""


def add_attribute(instance, member, val):
    """add attribute to an instance"""
    if hasattr(instance, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(instance, member, val)
