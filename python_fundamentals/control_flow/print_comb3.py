#!/usr/bin/env python3

result = []

for first in range(10):
    for second in range(first + 1, 10):
        result.append("{:02d}".format((first * 10) + second))

print(", ".join(result))
