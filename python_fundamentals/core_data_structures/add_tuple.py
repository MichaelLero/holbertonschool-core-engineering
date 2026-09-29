#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Add (0, 0) to guarantee 2+ elements, then take only the first 2 [:2]
    a = (tuple_a + (0, 0))[:2]  # e.g., (1,) becomes (1, 0)
    b = (tuple_b + (0, 0))[:2]  # e.g., ()   becomes (0, 0)

    # Add index 0 to index 0, and index 1 to index 1
    return (a[0] + b[0], a[1] + b[1])
