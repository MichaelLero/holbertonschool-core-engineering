#!/usr/bin/env python3

def print_last_digit(number):
    digit_str = str(number)
    last_digit = digit_str[-1]
    digit = int(last_digit)
    print(digit, end="")
    return digit
