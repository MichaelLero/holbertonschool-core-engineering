#!/usr/bin/env python3

result = []

for first in range(10):
    for second in range(first + 1, 10):
        formatted_pair = "{:01d}{:01d}".format(first, second)
        result.append(formatted_pair)

output = ", ".join(result)
print(output)
