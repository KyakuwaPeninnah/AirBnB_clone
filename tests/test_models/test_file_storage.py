#!/usr/bin/env python3
"""Unittests for the FileStorage class."""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.isfile(self.file_path):
            os.rename(self.file_path, self.file_path + ".bak")
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.user = User()

    def tearDown(self):
        """Clean up test environment."""
        if os.path.isfile(self.file_path):
            os.remove(self.file_path)
        if os.path.isfile(self.file_path + ".bak"):
            os.rename(self.file_path + ".bak", self.file_path)
        del self.storage

    def test_all(self):
        """Test the all method."""
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)

    def test_new(self):
        """Test the new method."""
        self.storage.new(self.obj)
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.obj)

    def test_save(self):
        """Test the save method."""
        self.storage.new(self.obj)
        self.storage.save()
        with open(self.file_path, "r", encoding="utf-8") as f:
            content = json.load(f)
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.assertIn(key, content)
        self.assertEqual(content[key], self.obj.to_dict())

    def test_reload(self):
        """Test the reload method."""
        self.storage.new(self.obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].to_dict(), self.obj.to_dict())

    def test_reload_no_file(self):
        """Test reload method when no file exists."""
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

if __name__ == "__main__":
    unittest.main()

