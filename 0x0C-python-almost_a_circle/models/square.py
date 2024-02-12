#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """initializing the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """square Class constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """over loading method that returns the square info"""

        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """square Size getter"""

        return self.width

    @size.setter
    def size(self, value):
        """square size setter"""

        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """an internal method that updates instance attributes"""

        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """
        public method that assigns attributes with,
        keyworded arguments and no-keyworded arguments.
        *args is the list of arguments - no-keyworded arguments
        **kwargs can be thought of as a double pointer,
        to a dictionary: key/value (keyworded arguments).
        **kwargs must be skipped if *args exists and is not empty.
        """

        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """
        public method  that returns the dictionary representation of a Square
        """

        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
