# test_textlib.py


import unittest
from textlib import BodyOfText, Paragraph

# set of anomaly strings:
anomaly1 = "     "
anomaly2 = """     
                    
     """

string0 = ""  # 0 sentences
expected0 = [""]

string1 = """This is a one paragraph string."""  # 1 sentence
expected1 = ["This is a one paragraph string."]

string12 = """This is a one paragraph string.
"""

# string3 has 6 sentences
string3 = """This is a rather short story. It has three paragraphs.

Once upon a time, a brave princess went on a dangerous journey. She
had many adventures, and recruited other heroes to her important and
noble cause.

She prevailed, saving the day, and made it home. Yay!"""

string31 = """This is a paragraph 1.

Paragraph 2.

And, paragraph 3!"""

expected31 = ["This is a paragraph 1.", "Paragraph 2.", "And, paragraph 3!"]

# complex_string has 5 sentences
complex_string = """Mr. Smith bought cheap_site.com for 1.5 million dollars, 
i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true...
 Well, with a probability of .98, it isn't!
"""

# some other rather complex sentences
cplx_str1 = """
    My favorite website is docs.python.org, with reddit.com coming in a close second.
"""
tricky_str = "I bought a basket of fruit for Mrs. Smith's birthday."
cplx_str3 = "I will arrive between 6 a.m. and 7 a.m."
cplx_str4 = "Your total is $10.43."
cplx_str5 = "Yay! We made it. High five!"

tricky_str2 = """Did you tell Mr. Burke yesterday before 9 p.m.? Mrs. Burke and Ms. Edwards are bringing the
birthday cake tomorrow at approximately 10 a.m."""

para0 = Paragraph(string0)
para1 = Paragraph(string1)
para5 = Paragraph(string3)
para_complex = Paragraph(complex_string)
c_str1 = Paragraph(cplx_str1)
tricky = Paragraph(tricky_str)
c_str3 = Paragraph(cplx_str3)
c_str4 = Paragraph(cplx_str4)
c_str5 = Paragraph(cplx_str5)
tricky2 = Paragraph(tricky_str2)


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


class TestParagraph(unittest.TestCase):
    def test_empty_paragraph(self):
        self.assertEqual(0, para0.num_sentences())

    def test_single_sentence(self):
        """test for single sentence in paragraph"""
        self.assertEqual(1, para1.num_sentences())

    def test_several_sentences(self):
        """test for at least three sentences in paragraph"""
        self.assertEqual(6, para5.num_sentences())

    def test_complex_sentences(self):
        """test for a complex set of sentences in paragraph"""
        self.assertEqual(5, para_complex.num_sentences())
        self.assertEqual(1, c_str1.num_sentences())
        self.assertEqual(1, tricky.num_sentences())
        self.assertEqual(1, c_str3.num_sentences())
        self.assertEqual(1, c_str4.num_sentences())
        self.assertEqual(2, c_str5.num_sentences())
        self.assertEqual(2, tricky2.num_sentences())


# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
