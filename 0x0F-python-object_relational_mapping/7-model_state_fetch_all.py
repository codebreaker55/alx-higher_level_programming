#!/usr/bin/python3
"""module that lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State

    sav = sys.argv
    if len(sav) < 4:
        exit(1)
    # connect to a MySQL server running on localhost at port 3306
    s_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(s_str.format(sav[1], sav[2], sav[3]))
    Session = sessionmaker(bind=engine)

    # create tables if they do not exist
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # query and print State data
    output = session.query(State).order_by(State.id).all()
    for state in output:
        print("{}: {}".format(state.id, state.name))

    session.close()
