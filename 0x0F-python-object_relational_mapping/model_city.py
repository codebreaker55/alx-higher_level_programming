#!/usr/bin/python3
"""module that contains the class definition of a State
and an instance Base = declarative_base()"""
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City class:
        inherits from Base (imported from model_state)
        links to the MySQL table cities
        class attribute id that represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key
        class attribute name that represents a column of a string
        of 128 characters, and can’t be null
        class attribute state_id that represents a column of an integer,
        can’t be null and is a foreign key to states.id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
