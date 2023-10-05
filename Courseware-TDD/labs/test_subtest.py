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
            "foo    \t    \t",
            " \tfoo bar",
        ]
        for text in texts:
            with self.subTest(text=text):
                self.assertEqual(1, Whitespace(text).whitespace_subtest())
