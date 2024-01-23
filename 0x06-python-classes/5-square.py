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

    def my_print(self):
        """Public instance method that prints in stdout
        the square with the character #"""

        for n in range(self.size):
            for m in range(self.size):
                print("#", end="\n" if n is self.size - 1 and n != m else "")
        print()
