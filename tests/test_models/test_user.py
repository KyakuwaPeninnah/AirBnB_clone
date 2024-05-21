#!/usr/bin/env python3
"""Unittests for the User class."""


import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test the User class."""

    def setUp(self):
        """Set up test environment."""
        self.user = User()

    def tearDown(self):
        """Clean up test environment."""
        del self.user

    def test_is_instance(self):
        """Test if user is an instance of BaseModel."""
        self.assertIsInstance(self.user, User)

    def test_email_attr(self):
        """Test that the email attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertEqual(self.user.email, "")

    def test_password_attr(self):
        """Test that the password attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertEqual(self.user.password, "")

    def test_first_name_attr(self):
        """Test that the first_name attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attr(self):
        """Test that the last_name attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.last_name, "")

    def test_id_is_unique(self):
        """Test that each User instance has a unique id."""
        user2 = User()
        self.assertNotEqual(self.user.id, user2.id)

    def test_to_dict(self):
        """Test the to_dict method of the User class."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertEqual(user_dict['first_name'], self.user.first_name)
        self.assertEqual(user_dict['last_name'], self.user.last_name)
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

if __name__ == "__main__":
    unittest.main()

