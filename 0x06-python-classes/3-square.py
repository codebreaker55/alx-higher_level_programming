#!/usr/bin/python3
"""Initializing a class"""


class Square:
    """Defining the size within the square class"""

    def __init__(self, size=0):
        """Inizializing the conditions for Private instance attribute: size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """a Public instance method that returns the current square area"""

        return self.__size * size
