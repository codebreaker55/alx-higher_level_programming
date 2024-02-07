#!/usr/bin/python3
"""load_from_json_file module"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""

    with open(fileaname, "r", encoding="utf-8") as fil:
        return json.load(fil)
