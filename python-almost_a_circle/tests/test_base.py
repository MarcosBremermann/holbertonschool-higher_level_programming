#!/usr/bin/python3
"""
Unittest for class Base methods
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Class that tests Base
    """
    def test_base_id(self):
        """
        Test if the Base class initializes
        with the correct ID
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_base_custom_id(self):
        """
        Test if the Base class initializes
        with a custom ID
        """
        b2 = Base(100)
        self.assertEqual(b2.id, 100)

    def test_base_multiple_instances(self):
        """
        Test if multiple instances get
        unique IDs
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)

    def test_to_json_string_empty(self):
        """
        Test if to_json_string returns
        an empty list when no input
        """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string(self):
        """
        Test if to_json_string returns
        the correct JSON representation
        """
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]')

    def test_from_json_string_empty(self):
        """
        Test if from_json_string returns an
        empty list when the input is []
        """
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string(self):
        """
        Test if from_json_string returns
        the correct list
        """
        json_str = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]'
        result = Base.from_json_string(json_str)
        expected = [{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
