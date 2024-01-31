#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n, count = 0, 0
    while n < x:
        try:
            print("{:d}".format(my_list[n]), end='')
            count = count + 1
        except (TypeError, ValueError):
            pass
        n = n + 1
    print()
    return count
