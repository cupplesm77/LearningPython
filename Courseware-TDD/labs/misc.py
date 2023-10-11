# misc.py

import re
from collections import Counter
from dataclasses import dataclass


@dataclass
class Datastore:
    name: str

    def bmethod(self):
        test_var = int("22")
        return test_var


# exercise in classes
@dataclass
class Aclass(Datastore):
    name: str

    def amethod(self):
        x = self.bmethod()
        return x


test_data = Datastore("Datastore")
aclass = Aclass("Aclass")
print(f"Hello, my name is {aclass.name}")
print(f"{aclass.name}'s data = {aclass.amethod()}")
print(f"I use a class named {test_data.name} that stores data for me.")


y = []
for x in range(10):
    y.append(x)
# extract the last 5 records from y
print(y)
record = 5
y_lastfive = y[-record:]
print(y_lastfive)

# parsing a dictionary
pattern = "[,;.!?]"
test_items = [
    {
        "text": "This is a sentence.",
        "counts": {"this": 1, "is": 1, "a": 1, "sentence": 1},
    },
    {
        "text": "Truth is beauty; beauty, truth.",
        "counts": {"truth": 2, "beauty": 2, "is": 1},
    },
    {
        "text": "I could finally SEE. But what I could see, remained a mystery.",
        "counts": {
            "i": 2,
            "could": 2,
            "finally": 1,
            "see": 2,
            "but": 1,
            "what": 1,
            "remained": 1,
            "a": 1,
            "mystery": 1,
        },
    },
]


def wordcounts(regex_pattern, **kwargs):
    # print(kwargs)
    counter_text = kwargs["text"].lower()
    remove_punctuation = re.sub(regex_pattern, "", counter_text).strip()
    # print(remove_punctuation)
    text_list = remove_punctuation.split()
    x_counter = Counter(text_list)
    count_dict = dict(x_counter)
    count_dict = dict(
        sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
    )
    return count_dict


for item in test_items:
    expected = item["counts"]
    count_words = wordcounts(pattern, text=item["text"])
    print(expected)
    print(count_words)


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


print(counter_text)
text_new = re.sub("[.!?;:,]", "", counter_text)
print(text_new)
counter = {}
for letter in text_new:
    if letter != " ":
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
print(counter)
counter_sorted = dict(sorted(counter.items(), key=lambda itm: itm[1], reverse=True))
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


text = """    WOW...! I could finally SEE: But what I could see, remained 
        a mystery! """
print(text)
text1 = text.lower().strip()
print(text1)
text2 = re.sub("[.?!,;:\n]", "", text1).split()
print(text2)
count = dict(Counter(text2))
print(count)
count_dict = dict(sorted(count.items(), key=lambda itm: itm[1], reverse=True))
print(count_dict)
