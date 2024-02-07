#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    Returns: the number of characters written
    """

    with open(filename, "w", encoding="utf-8") as fil:
        return (fil.write(text))
