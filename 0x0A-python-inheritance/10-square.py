#!/usr/bin/python3
"""Rectangle class module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """insertation of square subclass that represents a rectangle"""

    def __init__(self, size):
        """
        Instantiation with size
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """initializing area of square method"""

        return self.__size * self.__size
