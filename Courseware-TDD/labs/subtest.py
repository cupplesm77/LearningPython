# subtest.py

import re


class Whitespace:
    def __init__(self, text):
        if text == "":
            raise ValueError("text must not be an empty string")
        self.text = text

    def whitespace_subtest(self):
        pattern = "\s+"
        remove_white = re.sub(pattern, " ", self.text).strip()
        count = remove_white.count(" ")
        print(f"remove_white = {remove_white}")
        return count
