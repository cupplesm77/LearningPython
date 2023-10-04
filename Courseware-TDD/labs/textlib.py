# textlib.py

import re

# pattern for finding sentences
pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"


class Paragraph:
    null_string = ""
    _words_with_period = {"a.m.", "p.m.", "Mr.", "Mrs.", "Ms."}

    def __init__(self, text):
        self.text = text

    def num_sentences(self):
        t_str = self.text
        for wrd in self._words_with_period:
            all_words = re.findall(wrd, t_str)
            if all_words:
                print(all_words)
                t_str = t_str.replace(wrd, "#####")
                # all_words = []
        print(t_str)
        split_string = re.split(pattern, t_str)
        if self.null_string not in split_string:
            pass
        else:
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
            raise ValueError("text can not be empty")
        else:
            count = self.text.count(self.split_str_paragraphs)
            number_paragraphs = count + 1
            return number_paragraphs

    def paragraphs(self):
        par_list = self.text.split(self.split_str_paragraphs)
        return par_list


# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
