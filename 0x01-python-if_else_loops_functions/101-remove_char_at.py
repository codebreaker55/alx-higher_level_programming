#!/usr/bin/python3
def remove_char_at(str, n):
    n_str = ""
    for ind, ch in enumerate(str):
        if ind != n:
            n_str = n_str + ch
    return n_str
