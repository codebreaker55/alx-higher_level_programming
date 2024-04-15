#!/usr/bin/python3
"""module that deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


if __name__ == "__main__":
    sav = sys.argv
    # connect to a MySQL server running on localhost at port 3306
    s_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(s_str.format(sav[1], sav[2], sav[3]))
    Session = sessionmaker(bind=engine)

    # create tables if they do not exist
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # deleting all State objects with a name containing the letter 'a'
    for inst in session.query(State).filter(State.name.like('%a%')):
        session.delete(inst)
    session.commit()
