#!/usr/bin/python3
"""
test_square.py - Test cases for the Square class.
"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_str(self):
        s = Square(3, 2, 1, 5)
        self.assertEqual(str(s), "[Square] (<5>) <2>/<1> - <3>")

    def test_update(self):
        s = Square(3, 2, 1, 5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (<10>) <2>/<1> - <3>")
        s.update(20, 4)

    def test_to_dictionary(self):
        s = Square(3, 2, 1, 5)
        d = s.to_dictionary()
        expected = {
            'id': 5,
            'x': 2,
            'y': 1,
            'size': 3
        }
        self.assertEqual(d, expected)

if __name__ == '__main__':
    unittest.main()
