import json
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Clean up test environment"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new(self):
        """Test new method"""
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all())

    def test_all(self):
        """Test all method"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn(self.model, all_objects.values())

    def test_save(self):
        """Test save method"""
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r", encoding="utf-8") as file:
            content = json.load(file)
            key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
            self.assertIn(key, content)

    def test_reload(self):
        """Test reload method"""
        self.storage.save()
        FileStorage._FileStorage__objects = {}
        self.assertEqual(len(self.storage.all()), 0)
        self.storage.reload()
        self.assertGreater(len(self.storage.all()), 0)
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)


if __name__ == '__main__':
    unittest.main()
