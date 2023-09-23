#!/usr/bin/python3
""" Module for Review Model class for the HBNB project """
from models.base_model import BaseModel, Base
from os import getenv


class Review(BaseModel, Base):
    """Review classto store review information"""

    __tablename__ = "reviews"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        pass

    else:
        place_id = ""
        user_id = ""
        text = ""
