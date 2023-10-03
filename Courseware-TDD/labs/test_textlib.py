import unittest
from textlib import BodyOfText

string0 = ""
expected0 = [""]

string1 = """This is a one paragraph string"""
expected1 = ["This is a one paragraph string"]

string12 = """This is a one paragraph string
"""

string3 = """This is a rather short story. It has three paragraphs.

Once upon a time, a brave princess went on a dangerous journey. She
had many adventures, and recruited other heroes to her important and
noble cause.

She prevailed, saving the day, and made it home. Yay!"""

string31 = """This is a paragraph 1.

Paragraph 2.

And, paragraph 3!"""

expected31 = ["This is a paragraph 1.", "Paragraph 2.", "And, paragraph 3!"]


class TestBodyOfText(unittest.TestCase):
    def test_empty_story(self):
        with self.assertRaises(ValueError):
            BodyOfText(string0).num_paragraphs()
        # self.assertEqual(0, BodyOfText(string0).num_paragraphs())
        # self.assertEqual(expected0, BodyOfText(string0).paragraphs())

    def test_single_paragraph1(self):
        self.assertEqual(1, BodyOfText(string1).num_paragraphs())
        self.assertEqual(expected1, BodyOfText(string1).paragraphs())

    def test_single_paragraph12(self):
        self.assertEqual(1, BodyOfText(string12).num_paragraphs())

    def test_several_paragraphs(self):
        self.assertEqual(3, BodyOfText(string3).num_paragraphs())
        self.assertEqual(expected31, BodyOfText(string31).paragraphs())


# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
