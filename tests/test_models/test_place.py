#!/usr/bin/env python3
"""Unittests for the Place class."""


import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test the Place class."""

    def setUp(self):
        """Set up test environment."""
        self.place = Place()

    def tearDown(self):
        """Clean up test environment."""
        del self.place

    def test_is_instance(self):
        """Test if place is an instance of BaseModel."""
        self.assertIsInstance(self.place, Place)

    def test_city_id_attr(self):
        """Test that the city_id attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertEqual(self.place.city_id, "")

    def test_user_id_attr(self):
        """Test that the user_id attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertEqual(self.place.user_id, "")

    def test_name_attr(self):
        """Test that the name attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertEqual(self.place.name, "")

    def test_description_attr(self):
        """Test that the description attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertEqual(self.place.description, "")

    def test_number_rooms_attr(self):
        """Test that the number_rooms attribute exists and is initialized to 0."""
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test that the number_bathrooms attribute exists and is initialized to 0."""
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test that the max_guest attribute exists and is initialized to 0."""
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test that the price_by_night attribute exists and is initialized to 0."""
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude_attr(self):
        """Test that the latitude attribute exists and is initialized to 0.0."""
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude_attr(self):
        """Test that the longitude attribute exists and is initialized to 0.0."""
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids_attr(self):
        """Test that the amenity_ids attribute exists and is an empty list."""
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertEqual(self.place.amenity_ids, [])

    def test_id_is_unique(self):
        """Test that each Place instance has a unique id."""
        place2 = Place()
        self.assertNotEqual(self.place.id, place2.id)

    def test_to_dict(self):
        """Test the to_dict method of the Place class."""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['city_id'], self.place.city_id)
        self.assertEqual(place_dict['user_id'], self.place.user_id)
        self.assertEqual(place_dict['name'], self.place.name)
        self.assertEqual(place_dict['description'], self.place.description)
        self.assertEqual(place_dict['number_rooms'], self.place.number_rooms)
        self.assertEqual(place_dict['number_bathrooms'], self.place.number_bathrooms)
        self.assertEqual(place_dict['max_guest'], self.place.max_guest)
        self.assertEqual(place_dict['price_by_night'], self.place.price_by_night)
        self.assertEqual(place_dict['latitude'], self.place.latitude)
        self.assertEqual(place_dict['longitude'], self.place.longitude)
        self.assertEqual(place_dict['amenity_ids'], self.place.amenity_ids)
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)

if __name__ == "__main__":
    unittest.main()

