#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry:
    """inizializing BaseGeometry class"""

    def area(self):
        """
        a public instance method that raises an Exception
        with the message: area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
