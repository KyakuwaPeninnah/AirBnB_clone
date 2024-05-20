#!/usr/bin/python3
"""This module handles the review of the bookings"""

from models.base_model import BaseModel

class Review(BaseModel):
    """The review class manages the review objects"""

    place_id = ""
    user_id = ""
    text = ""
