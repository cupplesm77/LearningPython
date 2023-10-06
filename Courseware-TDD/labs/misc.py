# misc.py

import re
from collections import Counter

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

counter_text = "Truth is beauty; beauty, truth"
counter_text = counter_text.lower()
pattern = "[,;.!?]"
remove_sep = re.sub(pattern, "", counter_text).strip()
print(remove_sep)
# using Counter from collections
x = remove_sep.split()
x_counter = Counter(x)
print(dict(x_counter))


counter = {}
for letter in counter_text:
    if letter != " ":
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
print(counter)
counter_sorted = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
print(counter_sorted)


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
