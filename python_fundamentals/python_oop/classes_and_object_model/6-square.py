#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Defines a square object."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position offset (x, y) of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' taking position offsets into account."""
        if self.__size == 0:
            print("")
            return

        # Print vertical offset (y-coordinate)
        for _ in range(self.__position[1]):
            print("")

        # Print square rows with horizontal offset (x-coordinate)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns the string representation of the square."""
        if self.__size == 0:
            return ""

        output = []
        # Add vertical offset (y-coordinate)
        for _ in range(self.__position[1]):
            output.append("")

        # Add square rows with horizontal offset (x-coordinate)
        for _ in range(self.__size):
            output.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(output)
