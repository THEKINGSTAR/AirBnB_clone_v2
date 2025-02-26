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
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")

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

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Getter attribute to return a list of Review instances
            where place_id equals to the current Place.id for FileStorage"""
            from models import storage
            reviews_list = []
            all_reviews = storage.all("Review")
            for review in all_reviews.values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
