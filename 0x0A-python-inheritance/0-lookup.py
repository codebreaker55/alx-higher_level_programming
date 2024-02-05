#!/usr/bin/python3
"""lookup function module"""


def lookup(obj):
    """ function that returns the list of available attributes
        and methods of an object
        Args:
            obj: is the object to be listed

        Returns:
                a list object
    """

    return dir(obj)
