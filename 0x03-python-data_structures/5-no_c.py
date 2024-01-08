#!/usr/bin/env python3
def no_c(my_string):
    strin = ""
    for ch in my_string:
        if (ch != 'c' and ch != 'C'):
            strin = strin + ch
    return strin

