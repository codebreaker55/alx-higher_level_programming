#!/usr/bin/python3
"""student class module"""


class Student:
    """a class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        puplic method that retrieves a dictionary representation,
        of a Student instance
        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved, Otherwise, all attributes must be retrieved
        """

        try:
            for atr in attrs:
                if type(atr) is not str:
                    return (self.__dict__)
        except Exception:
            return (self.__dict__)
        new_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return (new_dict)
