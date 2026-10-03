#!/usr/bin/env python3

"""
Module that defines a Square class.
"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance."""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        pass
