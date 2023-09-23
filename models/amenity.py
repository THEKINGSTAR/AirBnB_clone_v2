#!/usr/bin/python3
"""
Amenity (models/amenity.py):
Public class attributes:
name: string
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv


class Amenity(BaseModel, Base):
    """Amenity class (models/amenity.py)"""

    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
