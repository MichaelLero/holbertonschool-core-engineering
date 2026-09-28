#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    # Loop through each sublist (row) in the 2D matrix
    for row in matrix:
        # Format each integer using {:d} and join them with spaces,
        # then print the row
        print(" ".join("{:d}".format(i) for i in row))
