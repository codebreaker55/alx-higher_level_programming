#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    were obj is an instance of a Class
    """

    return (obj.__dict__)
