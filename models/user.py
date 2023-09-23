#!/usr/bin/python3
"""This module for User class Model that inherits
 from BaseModel and Base:
location: models/user.py
Public class attributes:
email: string - empty string
password: string - empty string
first_name: string - empty string
last_name: string - empty string
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user class
    that have user related attributes"""

    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            "Place", backref="user", cascade="all, delete, delete-orphan"
                )

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
