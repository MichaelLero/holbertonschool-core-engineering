#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Call str.format(template, data) explicitly
        output = str.format("{}", row)
        print(output)
