#!/usr/bin/env python3

# txt is our string
txt = "{} = {:#x}"

# our inputs
for i in range(0, 98+1):
    print(txt.format(i, i))
