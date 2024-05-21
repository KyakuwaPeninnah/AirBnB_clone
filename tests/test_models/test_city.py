#!/usr/bin/env pythion3
"""Unittests for the City class."""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test the City class."""

    def setUp(self):
        """Set up test environment."""
        self.city = City()

    def tearDown(self):
        """Clean up test environment."""
        del self.city

    def test_is_instance(self):
        """Test if city is an instance of BaseModel."""
        self.assertIsInstance(self.city, City)

    def test_state_id_attr(self):
        """Test that the state_id attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.state_id, "")

    def test_name_attr(self):
        """Test that the name attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.name, "")

    def test_id_is_unique(self):
        """Test that each City instance has a unique id."""
        city2 = City()
        self.assertNotEqual(self.city.id, city2.id)

    def test_to_dict(self):
        """Test the to_dict method of the City class."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], self.city.state_id)
        self.assertEqual(city_dict['name'], self.city.name)
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)

if __name__ == "__main__":
    unittest.main()
