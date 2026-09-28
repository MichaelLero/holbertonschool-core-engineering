#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # 1. Convert numbers to strings and join them with a space
        row_string = " ".join(map(str, row))
        # 2. Print using str.format() on the single line
        print(str.format("{}", row_string))
