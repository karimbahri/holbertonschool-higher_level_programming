#!/usr/bin/python3
"""list all objects from DB"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://\
                          {}:{}@localhost/{}'.format(sys.argv[1],
                                                     sys.argv[2],
                                                     sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for element in session.query(State).order_by(asc(State.id)):
        print("{}: {}".format(element.id, element.name))
    sess.close()
