#!/usr/bin/python3
"""adding new attribute method"""


def add_attribute(obj, att, value):
    """
    function that adds a new attribute to an object if it’s possible
    if the object can’t have new attribute: Raise a TypeError exception
    with the message can't add new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
