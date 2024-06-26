#!/bin/usr/python3
"""Filestorage module"""


from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.user import User
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_class_name = obj .__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serial_obj = {}
        for key, value in FileStorage.__objects.items():
            serial_obj[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serial_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                      "City": City, "Review": Review,
                      "Place": Place, "Amenity": Amenity}
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    content_file = json.load(f)
                    for key, value in content_file.items():
                        objects = FileStorage.__objects
                        objects[key] = class_dict[value["__class__"]](**value)
        except FileNotFoundError:
            pass
