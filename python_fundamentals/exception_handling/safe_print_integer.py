#!/usr/bin/env python3

def safe_print_integer(value):
    try:
        # will fail with a ValueError if 'value' is a
        # float or a non-numeric string
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
