#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """intializing the class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Private instance attributes, each with its own public,
        getter and setter"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width instance getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """Width instance setter"""

        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Height instance getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """Height instance setter"""

        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x instance getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """x instance setter"""

        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """y instance getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """y instance setter"""

        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """validation of all setter methods and instantiation except id"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
        public method that returns the area value of the Rectangle instance
        """

        return self.width * self.height

    def display(self):
        """ public method that prints in stdout the Rectangle instance
        with the character #"""

        dis = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(dis, end='')

    def __str__(self):
        """method that returns rectangle class info"""

        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """public method  that assigns an argument to each attribute"""

        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """public method that assigns a key/value argument to attributes"""

        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """public method that returns the dictionary representation
        of a Rectangle"""

        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
