#!/usr/bin/env python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
    # max() loops through keys ('John', 'Bob'...),
    # but compares their values (12, 14...)

    # using a_dictionary.get to find and return the key with the highest score.
