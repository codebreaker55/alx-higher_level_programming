#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """Instantiation with optional width and height"""

    def __init__(self, width=0, height=0):
        """defining width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """using getter to retrieve the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """using setter to set exceptions"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """using getter to retrieve the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """using setter to set exceptions"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """instance method that returns the rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """instance method that returns the rectangle perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the rectangle with the character #"""

        s = ""
        if self.__width != 0 and self.__height != 0:
            s = s + "\n".join("#" * self.__width for h in range(self.__height))
        return s

    def __repr__(self):
        """return a string representation of the rectangle"""

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
