#!/usr/bin/python3
"""MyList class module"""


class MyList(list):
    """intializing mylist class that inherits from list"""

    def print_sorted(self):
        """inizializing Public instance method that prints the list sorted"""

        print(sorted(self))
