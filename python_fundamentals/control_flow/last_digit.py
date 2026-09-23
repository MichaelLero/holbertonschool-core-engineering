#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)

# converts the integer into a string
digit_str = str(number)

# pulling last digit
last_digit = digit_str[-1]

# convert back to an integer
digit = int(last_digit)

if digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")

if digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")

if digit < 6 and digit != 0:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
