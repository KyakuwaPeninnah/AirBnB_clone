#!/usr/bin/env python3
"""Unittests for the Amenity class."""


import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test the Amenity class."""

    def setUp(self):
        """Set up test environment."""
        self.amenity = Amenity()

    def tearDown(self):
        """Clean up test environment."""
        del self.amenity

    def test_is_instance(self):
        """Test if amenity is an instance of BaseModel."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_name_attr(self):
        """Test that the name attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_id_is_unique(self):
        """Test that each Amenity instance has a unique id."""
        amenity2 = Amenity()
        self.assertNotEqual(self.amenity.id, amenity2.id)

    def test_to_dict(self):
        """Test the to_dict method of the Amenity class."""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], self.amenity.name)
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)

if __name__ == "__main__":
    unittest.main()
