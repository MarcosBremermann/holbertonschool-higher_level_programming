import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_generation(self):
        # Create two instances of the Base class
        obj1 = Base()
        obj2 = Base()

        # Check that the 'id' attributes are unique and incrementing
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_custom_id(self):
        # Create an instance of the Base class with a custom ID
        obj = Base(100)

        # Check that the 'id' attribute is set to the custom value
        self.assertEqual(obj.id, 100)

if __name__ == '__main__':
    unittest.main()
