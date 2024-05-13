#!/usr/bin/python3
"""Test module for base_model class"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseModel class that inherits from the unittest"""

    @classmethod
    def setUpClass(cls):
        """Class method that initializes a class instance"""
        cls.my_model = BaseModel()

    def test_init(self):
        """Initialises an instance"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsNotNone(self.my_model.id)
        self.assertIsNotNone(self.my_model.created_at)
        self.assertIsNotNone(self.my_model.updated_at)

    def test_str(self):
        """str method that prints class name, id and dict"""
        expected_str = "[BaseModel] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_save(self):
        """updates public attribute instance"""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        new_updated_at = self.my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """returns a dictionary containing all keys/values"""
        my_dict = self.my_model.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)


if __name__ == '__main__':
    unittest.main()
