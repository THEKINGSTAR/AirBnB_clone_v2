#!/usr/bin/python3
""" State Model for HBNB project
Public class attributes:
name: string
cities represent a relationship between
State and City """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property  # cities getter attribute
        def cities(self):
            """if filestorage this define relationship
            between city and state
            returns the list of City instances with state_id
            equals to the current State.id"""
            from models import storage
            state_cities = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
