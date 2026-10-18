#!/usr/bin/env python3
"""Utility module for appending text to files."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return the character count.

    Args:
        filename (str): Path of the file to append to. It is created
            if it doesn't exist.
        text (str): The string to add to the end of the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
