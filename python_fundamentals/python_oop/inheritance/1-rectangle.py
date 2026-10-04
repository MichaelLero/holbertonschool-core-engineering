#!/usr/bin/env python3

"""Module that defines the base of different shape classes"""


class BaseGeometry:
    """class that defines the Base of geometry shapes"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class that inheriants from BaseGeometry"""

    def __init__(self, width=0, height=0):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
