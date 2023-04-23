#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarartive import declarative_base
from model_state import Base, State


class City(Base):
    """Empty class that inherits from Base"""
    __tablename__ == "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Integer, ForeignKey("states.id"), nullable=False)
