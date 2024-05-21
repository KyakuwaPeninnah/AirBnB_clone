#!/usr/bin/env python3
"""Unittests for the Review class."""


import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test the Review class."""

    def setUp(self):
        """Set up test environment."""
        self.review = Review()

    def tearDown(self):
        """Clean up test environment."""
        del self.review

    def test_is_instance(self):
        """Test if review is an instance of BaseModel."""
        self.assertIsInstance(self.review, Review)

    def test_place_id_attr(self):
        """Test that the place_id attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertEqual(self.review.place_id, "")

    def test_user_id_attr(self):
        """Test that the user_id attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertEqual(self.review.user_id, "")

    def test_text_attr(self):
        """Test that the text attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.text, "")

    def test_id_is_unique(self):
        """Test that each Review instance has a unique id."""
        review2 = Review()
        self.assertNotEqual(self.review.id, review2.id)

    def test_to_dict(self):
        """Test the to_dict method of the Review class."""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], self.review.place_id)
        self.assertEqual(review_dict['us

