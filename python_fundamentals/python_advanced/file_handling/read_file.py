#!/usr/bin/env python3

def read_file(filename=""):
    """Read a text file (UTF-8) and print its contents to stdout."""
    # Open the file in read mode, explicitly using UTF-8 encoding.
    # The "with" block closes the file automatically when we're done.
    with open(filename, "r", encoding="utf-8") as f:
        # Read the entire file into a single string
        content = f.read()
        # Print without adding an extra newline at the end,
        # so the output matches the file exactly
        print(content, end="")