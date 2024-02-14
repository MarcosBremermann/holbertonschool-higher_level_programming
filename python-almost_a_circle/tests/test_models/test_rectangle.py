#!/usr/bin/python3
"""
Unittest for the test of the rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
    Class for the testing of the  Rectangle class
    """

    def test_init_rectangle(self):
        """
        This function tests the initialization with a specified id.
        """
        test_rect = Rectangle(8, 7, 1000, 300, 33)
        self.assertEqual(test_rect.width, 8)
        self.assertEqual(test_rect.height, 7)
        self.assertEqual(test_rect.x, 1000)
        self.assertEqual(test_rect.y, 300)
        self.assertEqual(test_rect.id, 33)

    def test_width(self):
        """
        This function testes 3 different scenarios for width
        to either raise errors or execute correctly
        """
        test_width = Rectangle(10, 5)
        self.assertEqual(test_width.width, 10)
        with self.assertRaises(ValueError):
            test_width = Rectangle(-3, 5)
        with self.assertRaises(TypeError):
            test_width = Rectangle('This shouldnt work', 5)

    def test_height(self):
        """
        This function testes 3 different scenarios for height
        to either raise errors or execute correctly
        """
        test_height = Rectangle(10, 5)
        self.assertEqual(test_height.height, 5)
        with self.assertRaises(ValueError):
            test_height = Rectangle(3, -5)
        with self.assertRaises(TypeError):
            test_height = Rectangle(3, 'This shouldnt work')

    def test_x(self):
        """
        This function testes 3 different scenarios for x
        to either raise errors or execute correctly
        """
        test_x = Rectangle(10, 5, 8)
        self.assertEqual(test_x.x, 8)
        with self.assertRaises(ValueError):
            test_x = Rectangle(10, 5, -8)
        with self.assertRaises(TypeError):
            test_x = Rectangle(10, 5, "I'm not a number")

    def test_y(self):
        """
        This function testes 3 different scenarios for y
        to either raise errors or execute correctly
        """
        test_y = Rectangle(10, 5, 8, 7)
        self.assertEqual(test_y.y, 7)
        with self.assertRaises(ValueError):
            test_y = Rectangle(9, 4, 2, -6)
        with self.assertRaises(TypeError):
            test_y = Rectangle(9, 4, 2, "Not a number")

    def test_area(self):
        """
        This function testes the area of the rectangle
        """
        test_area = Rectangle(4, 6)
        self.assertEqual(test_area.area(), 24)
        test_area = Rectangle(10, 10, 5, 5)
        self.assertEqual(test_area.area(), 100)


if __name__ == '__main__':
    unittest.main()
