#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for ky in list(a_dictionary.keys()):
        if a_dictionary[ky] == value:
            del a_dictionary[ky]
    return a_dictionary
