#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    count = 0
    # Loop from 0 up to (x - 1)
    for i in range(0, x):
        try:
            # Attempt to print the element without moving to a new line
            print("{}".format(my_list[i]), end="")
        except IndexError:
            # Safely stop the loop if x is larger than the list length
            break
        else:
            # Only runs if the try block succeeds (element was printed)
            count += 1
    print()
    return count
