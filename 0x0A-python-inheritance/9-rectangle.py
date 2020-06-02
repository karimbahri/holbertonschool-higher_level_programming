#!/usr/bin/python3
"""
    5-base_geometry
        Classes:
            Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry: empty class"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area: return area"""
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """integer_validator: checks"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __str__(self):
        """str: string representation of rectangle instance"""
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string
