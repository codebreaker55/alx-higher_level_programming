#!/usr/bin/python3
"""Initializing Python class MagicClass"""


class MagicClass:
    """settinng the radius to 0"""

    def __init__(self, radius=0):
        """radius mut be a float or int"""

        self.__radius = 0

        if type(radius) is not float and type(radius) is not int:
            raise TypeError('radius must be a number')
        self.__radius = radius

        def area(self):
            """used to return the magic class area"""

            return self.__radius * self.__radius * math.pi

        def circumference(self):
            """it returns the circumference of the magic class"""

            return self.__radius * 2 * math.pi
