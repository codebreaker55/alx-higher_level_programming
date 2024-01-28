#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    """a and b must be integers or floats,
    otherwise raise a TypeError exception with the message
    a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b"""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
