# test_myrange.py

import unittest
from myrange import myrange


class TestMyrange(unittest.TestCase):
    def test_myrange(self):
        self.assertEqual([1, 3, 5, 7, 9], list(myrange(1, 10, 2)))
        self.assertEqual([1, 2, 3, 4, 5], list(myrange(1, 6)))
        self.assertEqual([-7, -4, -1, 2, 5], list(myrange(-7, 8, 3)))
        self.assertEqual([0, 1, 2, 3, 4], list(myrange(5)))
        self.assertEqual([3, 2, 1, 0, -1], list(myrange(3, -2, -1)))
        # test expected assertion errors
        # TypeError
        self.assertRaises(TypeError, lambda: list(myrange()))
        self.assertRaises(TypeError, lambda: list(myrange(1, 2, 1, 1)))
        self.assertRaises(TypeError, lambda: list(myrange(14.987)))
        self.assertRaises(TypeError, lambda: list(myrange('string')))
        # ValueError
        self.assertRaises(ValueError, lambda: list(myrange(5, 1, 1)))
        self.assertRaises(ValueError, lambda: list(myrange(5, -2, 1)))
        self.assertRaises(ValueError, lambda: list(myrange(-2, 5, -1)))

        # different formulation of a test case that does work
        # gen_obj1 = range(1, 2, 1, 1)
        # print(type(gen_obj1))
        gen_obj2 = myrange(1, 2, 1, 1)
        print(gen_obj2)

        # self.assertRaises(TypeError, lambda: next(gen_obj))
        # self.assertRaises(TypeError, next, gen_obj)
