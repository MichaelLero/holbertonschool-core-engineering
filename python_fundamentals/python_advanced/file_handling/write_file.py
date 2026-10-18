#!/usr/bin/env python3
"""Utility module for writing text to files."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the character count.

    Args:
        filename (str): Path of the file to write. It is created if it
            doesn't exist and overwritten if it does.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
