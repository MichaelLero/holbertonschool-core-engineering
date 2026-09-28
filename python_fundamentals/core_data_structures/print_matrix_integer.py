#!/usr/bin/env python3

# * unpacks elements as seperates arguements
# sep='\n' ensures a line break is placed between each item
def print_matrix_integer(matrix=[[]]):
    print(*matrix, sep='\n')
