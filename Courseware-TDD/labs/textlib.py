# textlib.py


class Paragraph:
    def __init__(self, text):
        pass

    def num_sentences(self):
        return -1


class BodyOfText:
    split_str = "\n\n"

    def __init__(self, text):
        self.text = text

    def num_paragraphs(self):
        if self.text == "":
            print(f"\ntext == {self.text}")
            print("assert ValueError: ")
            assert ValueError("text can not be empty string")
        else:
            count = self.text.count(self.split_str)
            number_paragraphs = count + 1
        return number_paragraphs

    def paragraphs(self):
        par_list = self.text.split(self.split_str)
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
