#!/usr/bin/python3
"""Base class module"""
from json import dumps, loads
import csv


class Base:
    """Base class representation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """if id is not None:
        assign the public instance attribute id with this argument value
        you can assume id is an integer
        otherwise:increment __nb_objects
        and assign the new value to the public instance attribute id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method that returns the JSON string representation"""

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """static methode that returns the list of the JSON string
        representation json_string"""

        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        a class method that writes the JSON string representation
        of list_objs to a file
        """

        if list_objs is not None:
            list_objs = [ob.to_dictionary() for ob in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as fl:
            fl.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """a class method that returns an instance with all attributes
        already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            n_dummy = Rectangle(1, 1)
        elif cls is Square:
            n_dumy = Square(1)
        else:
            n_dummy = None
        n_dummy.update(**dictionary)
        return n_dummy

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances"""
        from os import path

        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as fil:
            return [cls.create(**d) for d in cls.from_json_string(fil.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class method that serializes in CSV"""
        from models.rectangle import Rectangle
        from models.square import Square

        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[ob.id, ob.width, ob.height, ob.x, ob.y]
                             for ob in list_objs]
            else:
                list_objs = [[ob.id, ob.size, ob.x, ob.y]
                             for ob in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as fil:
            s_writer = csv.writer(fil)
            s_writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """class method that deserializes in CSV"""
        from models.rectangle import Rectangle
        from models.square import Square

        retrn = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as fil:
            l_reader = csv.reader(fil)
            for row in l_reader:
                row = [int(ele) for ele in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                retrn.append(cls.create(**d))
        return retrn

    @staticmethod
    def draw(list_rectangles, list_squares):
        """a static method that opens a window and draws
        all the Rectangles and Squares"""
        import turtle
        import time
        from random import randrange

        turtle.Screen().colormode(255)
        for ob in list_rectangles + list_squares:
            c = turtle.Turtle()
            c.color((randrange(255), randrange(255), randrange(255)))
            c.pensize(1)
            c.penup()
            c.pendown()
            c.setpos((ob.x + c.pos()[0], ob.y - c.pos()[1]))
            c.pensize(10)
            c.forward(i.width)
            c.left(90)
            c.forward(i.height)
            c.left(90)
            c.forward(i.width)
            c.left(90)
            c.forward(i.height)
            c.left(90)
            c.end_fill()

        time.sleep(5)
