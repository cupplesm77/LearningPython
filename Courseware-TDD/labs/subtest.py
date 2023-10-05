# subtest.py


class Whitespace:
    def __init__(self, text):
        if text == "":
            raise ValueError("text must not be an empty string")
        self.text = text

    def whitespace_subtest(self):
        return -1
