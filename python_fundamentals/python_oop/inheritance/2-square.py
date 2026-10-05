#!/usr/bin/env python3
"""Module that defines BaseGeometry, Rectangle and Square classes"""


class BaseGeometry:
    """Class that defines the base of geometry shapes"""

    def area(self):
        """Public instance method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer strictly"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize width and height after validating them"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize size after validating it"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates area"""
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
