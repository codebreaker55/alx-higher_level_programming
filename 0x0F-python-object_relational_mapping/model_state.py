#!/usr/bin/python3
"""module that contains the class definition of a State
and an instance Base = declarative_base()"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class:
    inherits from Base Tips
    links to the MySQL table states
    __tablename__ = 'states'
    class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
    class attribute name that represents a column of a string
    with maximum 128 characters and can’t be null.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
