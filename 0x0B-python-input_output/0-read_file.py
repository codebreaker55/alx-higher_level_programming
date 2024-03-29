#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, encoding='utf-8') as fil:
        print(fil.read(), end="")
