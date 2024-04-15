#!/usr/bin/python3
"""module that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State

    sav = sys.argv
    if len(sav) < 5 or ";" in sav[4]:
        exit(1)
    # connect to a MySQL server running on localhost at port 3306
    s_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(s_str.format(sav[1], sav[2], sav[3]))
    Session = sessionmaker(engine)

    # create tables if they do not exist
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # query and print State data
    output_query = session.query(State).filter(State.name.like(sav[4])).all()
    if len(output_query) == 0:
        print("Not found")
    else:
        print(output_query[0].id)

    session.close()
