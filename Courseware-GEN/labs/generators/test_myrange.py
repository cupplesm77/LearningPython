# test_myrange.py

import unittest
from myrange import myrange


class TestMyrange(unittest.TestCase):
    def test_myrange(self):
        self.assertEqual([1, 3, 5, 7, 9], list(myrange(1, 10, 2)))
        self.assertEqual([1, 2, 3, 4, 5], list(myrange(1, 6)))
        self.assertEqual([-7, -4, -1, 2, 5], list(myrange(-7, 8, 3)))
        self.assertEqual([0, 1, 2, 3, 4], list(myrange(5)))
        # test expected assertion errors
        self.assertRaises(ValueError, lambda: list(myrange()))
        self.assertRaises(ValueError, lambda: list(myrange(5, 1, 1)))
        self.assertRaises(ValueError, lambda: list(myrange(5, -2, 1)))
        self.assertRaises(ValueError, lambda: list(myrange(1, 2, 1, 1)))
        self.assertRaises(TypeError, lambda: list(myrange(14.987)))
        self.assertRaises(TypeError, lambda: list(myrange('string')))
