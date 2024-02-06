#!/usr/bin/python3
"""Rectangle class module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """initializing class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Instantiation with width and height
        width and height must be private. No getter or setter
        width and height must be positive integers
        validated by integer_validator
        """
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method of getting the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """function that represents rectangle description"""

        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
