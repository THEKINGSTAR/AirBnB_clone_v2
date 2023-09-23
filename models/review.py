#!/usr/bin/python3
""" Module for Review Model class for the HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Review classto store review information"""

    __tablename__ = "reviews"
    text = Column(String(128), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        pass

    else:
        place_id = ""
        user_id = ""
        text = ""
