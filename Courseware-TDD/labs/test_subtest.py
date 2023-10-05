# test_whitespace_subtest.py

# import
import unittest
from subtest import Whitespace


class TestWhitespace(unittest.TestCase):
    def test_whitespace_subtest(self):
        texts = [
            "",
            "foo bar",
            "    foo bar",
            "foo\tbar",
            "foo      bar",
            "foo    \t    \t bar",
            " \tfoo bar",
        ]
        for text in texts:
            if text == "":
                with self.assertRaises(ValueError):
                    Whitespace(text).whitespace_subtest()
            else:
                with self.subTest(text=text):
                    self.assertEqual(1, Whitespace(text).whitespace_subtest())
