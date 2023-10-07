# textlib.py

import re
from collections import Counter

# regex_pattern for finding sentences
pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"


class Paragraph:
    _null_string = ""
    _words_with_period = {"a.m.", "p.m.", "Mr.", "Mrs.", "Ms."}

    def __init__(self, text):
        self.text = text

    def num_sentences(self):
        t_str = self.text
        for wrd in self._words_with_period:
            all_words = re.findall(wrd, t_str)
            if all_words:
                t_str = t_str.replace(wrd, "#####")
        split_string = re.split(pattern, t_str)
        if self._null_string not in split_string:
            pass
        else:
            split_string.pop(split_string.index(""))
        count = len(split_string)
        return count


class BodyOfText:
    split_str_paragraphs = "\n\n"

    def __init__(self, text):
        if text == "":
            raise ValueError("text can not be an empty string")
        self.text = text

    def num_paragraphs(self):
        count = self.text.count(self.split_str_paragraphs)
        number_paragraphs = count + 1
        return number_paragraphs

    def paragraphs(self):
        par_list = self.text.split(self.split_str_paragraphs)
        return par_list

    def wordcounts(self, regex_pattern):
        counter_text = self.text.lower()
        remove_punctuation = re.sub(regex_pattern, "", counter_text).strip()
        text_list = remove_punctuation.split()
        # return {}
        return dict(Counter(text_list))


# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
