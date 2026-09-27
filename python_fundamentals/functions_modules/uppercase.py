#!/usr/bin/python3

def uppercase(str):
    # Iterate through each character in the string one by one
    for c in str:
        # Check if the character's ASCII value falls in the
        # lowercase range ('a' through 'z')
        if 97 <= ord(c) <= 122:
            # ord(c) converts character to ASCII integer (e.g., 'a' -> 97)

            # Subtracting 32 shifts it to the uppercase
            # ASCII range (e.g., 97 - 32 = 65)

            # chr() converts the uppercase integer back
            # to a character (e.g., 65 -> 'A')
            c = chr(ord(c) - 32)

        # Print the character without adding a newline (end="")
        print("{}".format(c), end="")

    # Print a single newline after the entire string has finished printing
    print("")
