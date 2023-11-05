# test_misc.py
import unittest
from misc import max_func, get_ab


class test_functions(unittest.TestCase):
    def test_max_func(self):
        alist = [12, -4, 7, 21, -33, 7]
        self.assertEqual(21, max_func(alist, key=None))
        self.assertEqual(-33, max_func(alist, key=abs))
        alist2 = ["12", "4", "-7", "21", "-33", "7"]
        self.assertEqual("21", max_func(alist2, key=int))
        dict = [{'a': 1, 'ab': 12, 'AAAAAAA': 7, 'cdf': 3},
                {'a': 2, 'ab': -20, 'AAAAAAA': 19, 'cdf': 2},
                {'a': 3, 'ab': 2, 'AAAAAAA': 9, 'cdf': 1},
                ]
        self.assertEqual({'a': 1, 'ab': 12, 'AAAAAAA': 7, 'cdf': 3}, max_func(dict, key=get_ab))

        if True:
            print("Congratulations:  All Tests Passed")