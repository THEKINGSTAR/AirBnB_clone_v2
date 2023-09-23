#!/usr/bin/python3
"""
Place Model class fir Airbnb project v2
"""
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table


class Place(BaseModel, Base):
    """Place class (models/place.py)"""

    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        pass

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
