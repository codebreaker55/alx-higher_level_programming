#!/usr/bin/env python3
def no_c(my_string):
    strin = ""
    for ch in range(len(my_string)):
        if my_string[ch] is not in ['c', 'C']:
            strin = strin + my_string[ch]
        return strin

