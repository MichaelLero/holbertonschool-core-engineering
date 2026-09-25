#!/usr/bin/env python3

txt = "{:02d}"

for i in range(99):
    print(txt.format(i), end=", ")
print("99")
