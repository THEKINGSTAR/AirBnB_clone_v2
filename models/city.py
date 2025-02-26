#!/usr/bin/python3
""" City Model for HBNB project
Public class attributes:
state_id: string - empty string: it will be the State.id
name: string - empty string
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """city Model class to define
    state ID and name columns or attributes
    based on storage type file or db"""

    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False, unique=True)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        # task 8
        places = relationship(
                'Place', backref="cities", cascade="all, delete, delete-orphan"
            )

    else:  # filestorage
        state_id = ""
        name = ""
