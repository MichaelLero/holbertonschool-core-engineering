#!/usr/bin/env python3

def pow(a, b):
    if b < 0:
        return 1 / pow(a, -b)
    results = 1
    for n in range(b):
        results *= a
    return results
