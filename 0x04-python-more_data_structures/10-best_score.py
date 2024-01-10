#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_ky = ""
    max_val = 0
    for ky, val in a_dictionary.items():
        if val > max_val:
            max_ky = ky
            max_val = val
    return max_ky
