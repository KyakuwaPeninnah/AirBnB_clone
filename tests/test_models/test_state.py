#!/usr/bin/python3
"""Unittests for the State class."""


from models.base_model import BaseModel
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test the State class."""

    def setUp(self):
        """Set up test environment."""
        self.state = State()

    def tearDown(self):
        """Clean up test environment."""
        del self.state

    def test_is_instance(self):
        """Test if state is an instance of BaseModel."""
        self.assertIsInstance(self.state, State)

    def test_name_attr(self):
        """Test that the name attribute exists and is an empty string."""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_id_is_unique(self):
        """Test that each State instance has a unique id."""
        state2 = State()
        self.assertNotEqual(self.state.id, state2.id)

    def test_to_dict(self):
        """Test the to_dict method of the State class."""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], self.state.name)
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)

if __name__ == "__main__":
    unittest.main()
