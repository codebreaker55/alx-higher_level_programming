#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    else:
        return a_dictionary
