#!/usr/bin/env python3

for first in range(10):
    for second in range(first + 1, 10):
        # Calculate the mathematical value
        value = (first * 10) + second

        # Determine whether to print a trailing comma or the final newline
        ending = ", " if value < 89 else "\n"

        # Format and output directly to the stream without
        # storing the characters
        print("{:02d}".format(value), end=ending)
