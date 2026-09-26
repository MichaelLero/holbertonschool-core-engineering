#!/usr/bin/env python3

result = []

for first in range(10):
    for second in range(first + 1, 10):
        result.append(f"{first}{second}")

output = ", ".join(result)

print(output)
