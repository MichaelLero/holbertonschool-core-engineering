#!/usr/bin/env python3
"""Module defining Rectangle class inheriting from BaseGeometry"""
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """class that inheriants from BaseGeometry"""

    def __init__(self, width=0, height=0):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
