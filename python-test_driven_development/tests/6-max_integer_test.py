#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""
Unittest for the max_integer function
"""


class TestMaxInteger(unittest.TestCase):
    """
    Class for the test of max_integer
    """

    def test_all_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_all_big_positive_numbers(self):
        self.assertEqual(max_integer([7, 4, 8, 12, 15, 9, 25]), 25)

    def test_all_negative_numbers(self):
        self.assertEqual(max_integer([-3, -1, -4, -6, -2]), -1)

    def test_all_big_negative_numbers(self):
        self.assertEqual(max_integer([-3, -80, -2004, -912, -69, -420]), -3)

    def test_nothing_in_list(self):
        self.assertIsNone(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
