#!/usr/bin/python3
"""module that prints all City objects from the database hbtn_0e_14_usa"""
import sys
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    sav = sys.argv
    # connect to a MySQL server running on localhost at port 3306
    s_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(s_str.format(sav[1], sav[2], sav[3]))
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # display the result
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print("{}: ({})  {}".format(state.name, city.id, city.name))
