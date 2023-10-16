#!/usr/bin/python3
"""
Unittest for class Rectangle methods
"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_width(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)

    def test_height(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.height, 5)

    def test_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_str(self):
        r = Rectangle(3, 4, 1, 2, 7)
        self.assertEqual(str(r), "[Rectangle] (7) 1/2 - 3/4")

if __name__ == '__main__':
    unittest.main()
