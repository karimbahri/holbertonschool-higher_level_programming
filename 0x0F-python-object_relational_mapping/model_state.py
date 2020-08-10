#!/usr/bin/python3
"""
class definition of a State
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """State table"""
    __tablename__ = "states"
    id = Column(Integer, nullable=False, unique=True,
                primary_key=True, auto_increment=True)
    name = Column(String(128), nullable=False)
