#!/usr/bin/python3
"""This module creates a class called user"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class is a user class that manages user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
