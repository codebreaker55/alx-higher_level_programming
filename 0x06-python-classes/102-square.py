#!/usr/bin/python3
"""Initializing a class"""


class Square:
    """Defining the size within the square class"""

    def __init__(self, size=0):
        """Inizializing the Private instance attribute: size"""

        self.__size = size

    @property
    def size(self):
        """initializing property to retrive the size
        that raises TypeError and ValueError"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """a Public instance method that returns the current square area"""

        return self.__size * self.__size

    def __eq__(self, other):
        return self.area() == other.area()

    def __nq__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
