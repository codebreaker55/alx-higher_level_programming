#!/usr/bin/python3
"""Initializing a class"""


class Square:
    """Defining the size within the square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Inizializing the Private instance attribute: size and position"""

        self.__size = size
        self.position = position

    @property
    def size(self):
        """initializing property to retrive the size
        that raises TypeError and ValueError"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """use Private instance attribute to retrieve position"""

        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """a Public instance method that returns the current square area"""

        return self.__size * self.__size

    def my_print(self):
        """Public instance method that prints in stdout
        the square with the character #"""

        if self.__size == 0:
            print("")
            return

        [print("") for n in range(0, self.__position[1])]
        for n in range(0, self.__size):
            [print(" ", end="") for m in range(0, self.__position[0])]
            [print("#", end="") for i in range(0, self.__size)]
            print("")
