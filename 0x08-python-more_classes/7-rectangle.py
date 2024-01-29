#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """Instantiation with optional width and height"""

    number_of_instances = 0
    """Public class attribute to count the number of instances"""

    print_symbol = '#'
    """Public class attribute, used as symbol for string representation"""

    def __init__(self, width=0, height=0):
        """defining width and height"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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

        return self.width * self.height

    def perimeter(self):
        """instance method that returns the rectangle perimeter"""

        if not self.width or not self.height:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """print the rectangle with the character #"""

        if not self.width or not self.height:
            return ""
        return((str(self.print_symbol) * self.width + "\n")
               * self.height)[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""

        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Print the message Bye rectangle... when an instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
