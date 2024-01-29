#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """Instantiation with optional width and height"""

    def __init__(self, width=0, height=0):
        """defining width and height"""

        self.width = width
        self.height = height


@property
def width(self):
    """using getter to retrieve the width"""

    return self.width


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
