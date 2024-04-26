#!/usr/bin/python3
"""module that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""
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

    # adding new state
    new_state = State(name='Louisiana')
    session.add(new_state)

    # adding new instance
    new_inst = session.query(State).filter_by(name='Louisiana').first()
    print(new_inst.id)

    session.commit()
