#!/usr/bin/python3
import sys



def safe_print_integer_err(value):
    int_val = True
    try:
        print("{:d}".format(value))
    except ValueError as err:
        print("Exception:", err, file =sys.stderr)
        int_val = False
    return int_val
