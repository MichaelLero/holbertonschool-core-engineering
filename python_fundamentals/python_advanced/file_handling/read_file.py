#!/usr/bin/env python3
"""Utility module for reading and displaying text files."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to stdout."""
    # Open in read mode with explicit UTF-8 encoding; the "with" block
    # closes the file automatically, even if an error occurs.
    with open(filename, "r", encoding="utf-8") as f:
        # Read the entire file into a single string
        content = f.read()
        # end="" stops print from adding an extra newline, so the output
        print(content, end="")
