# textlib.py

import re

pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"

string2 = """Mr. Smith bought cheapsite.com for 1.5 million dollars, 
i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true...
 Well, with a probability of .98, it isn't!
"""
# testing my understanding of the pattern (regex)
# split_string = re.split(pattern, string2)
# print(f"length of string = {split_string}")
# print(len(split_string))
# if "" in split_string:
#     idx = split_string.index("")
#     print(f"idx = {idx}")
#     split_string.pop(idx)
# print(split_string)
# print(f"length of clean string = {len(split_string)}")


class Paragraph:
    split_str_sentences = pattern
    null_string = ""

    def __init__(self, text):
        self.text = text

    def num_sentences(self):
        split_string = re.split(pattern, self.text)
        if self.null_string in split_string:
            split_string.pop(split_string.index(""))
        count = len(split_string)
        return count


class BodyOfText:
    split_str_paragraphs = "\n\n"

    def __init__(self, text):
        self.text = text

    def num_paragraphs(self):
        if self.text == "":
            print(f"\ntext == {self.text}")
            print("assert ValueError: ")
            assert ValueError("text can not be empty")
        else:
            count = self.text.count(self.split_str_paragraphs)
            number_paragraphs = count + 1
        return number_paragraphs

    def paragraphs(self):
        par_list = self.text.split(self.split_str_paragraphs)
        return par_list


# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
#     extra:
#  * Add a stub method called "paragraphs" to "BodyOfText", which
#    returns an empty list.
#  * Add assertions to "test_empty_story", "test_single_paragraph", and
#    "test_several_paragraphs" that check for a correct return value
#    when this method is called.
#  * Run the test and observe that it fails like it should. This is the
#    first checkpoint, so to speak.
#  * Change "BodyOfText.paragraphs" so the tests now
#    pass. This will be the next checkpoint.
#  * Look at your code for the "num_paragraphs" and "paragraphs"
#    methods. Is there some way you can simplify your code? If so,
#    refactor - notice how you can use the tests to verify you didn't
#    introduce any new bugs!
