#!/usr/bin/env python3

"""
Module that defines a Square class.
"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, char="#"):
        """Initialize a new Square instance."""
        self.__size = size
        self.char = char

    @property
    def size(self):
        """Getter: Allows outside code to read __size."""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter: Validates the value before updating __size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
            return

        for _ in range(self.size):
            print(self.char * self.size)
