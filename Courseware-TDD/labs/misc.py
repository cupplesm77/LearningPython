# misc.py

import re

# count the number of sentences in a simple sentence
text = """This is a longer story.

Once upon a time, there was a princess in a castle.

She grew up to be a famous dancer."""

print(f"string = {text}")
print("")

text_replace = text.replace("\n", " ")
print(f"string with new-lines removed = {text_replace}")

text_count_sentences = 1 + text_replace.count(". ")
print(f"number of sentences in text_replace = {text_count_sentences}")


# more regex

# regex for ONLY whitespace
pattern = "^\s*$"

# string with only whitespace
text1 = """             
            
        """
print(text1)
text1_search = re.search(pattern, text1)
print(f"text1_search = {text1_search}")
print("")
if text1_search:
    raise ValueError("Text must not be only whitespace")
else:
    print("Terrific! Text is not ONLY whitespace")


# a string with not only whitespace
text2 = """1st line             

        """
print(text2)
text2_search = re.search(pattern, text2)
print(f"text2_search = {text2_search}")
print("")
if text2_search:
    raise ValueError("Text must not be only whitespace")
else:
    print("Terrific! Text is not ONLY whitespace")

text = "   foo    \t    \t bar  "
print(text)
pattern = "\s+"
remove_white = re.sub(pattern, " ", text).strip()
print(remove_white)
