#!/usr/bin/python3
"""Base class modul"""


import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class that defines all common
    attributes/methods for other classes
    """

    def __init__(self):
        """Initializing instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """string representation of an instance"""
        return "[{}],({}),{}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates public instace"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
