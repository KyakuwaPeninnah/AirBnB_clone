#!/usr/bin/python3
"""This module handles the state class that inherits from the basemodel class"""

from models.base_model import BaseModel

class State(BaseModel):
    """This state class inherits from the basemodel and is the state of user"""
    name = ""
