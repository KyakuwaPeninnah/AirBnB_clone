#!/usr/bin/python3
""""This module handles the city of the user"""

from models.base_model import BaseModel

class City(BaseModel):
    """The city class that inherits from the basemodel class that shows users city"""

    state_id = ""
    name = ""
