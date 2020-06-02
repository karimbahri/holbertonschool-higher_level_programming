#!/usr/bin/python3
"""
    5-base_geometry
        Classes:
            BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry: empty class"""

    def area(self):
        """area: raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator: checks"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
