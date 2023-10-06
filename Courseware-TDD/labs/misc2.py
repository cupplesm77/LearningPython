# imports
import numpy as np
import re
from collections import defaultdict

np.random.seed(444)

x = np.random.choice([False, True], size=100000)

print(x.shape)
print(x.dtype)
print(x.size)
print(x)


# use a loop to count transitions from False to True
def count_transitions(y) -> int:
    count: int = 0
    ij_zip = zip(y[:-1], y[1:])
    for i, j in ij_zip:
        if j and not i:
            count += 1
    return count


count_transitions(x)

# use

# file for testing various snippets of code

# dictionaries
channels = ["ONE", "two", "three", "four", "five"]
mydict = {channel: set() for channel in channels}
print(f"my dictionary: {mydict}")
joe = 4
sally = object()
mydict["three"].add(joe)
mydict["five"].add(sally)
print(mydict)

# Other stuff

# file for testing various snippets of code

# dictionaries
channels = ["ONE", "two", "three", "four", "five"]
mydict = {channel: set() for channel in channels}
print(f"my dictionary: {mydict}")
joe = 4
sally = object()
mydict["three"].add(joe)
mydict["five"].add(sally)
print(mydict)

# using key functions

foods = [
    {"name": "strawberries", "calories": 33, "protein": 0.7},
    {"name": "waffles", "calories": 291, "protein": 8},
    {"name": "eggs", "calories": 155, "protein": 13},
    {"name": "chicken breast", "calories": 165, "protein": 31},
]


# select the food with the minimum/maximum amounts of protein
def protein_food(item):
    return item["protein"]


def calories_food(item):
    return item["calories"]


proteins = (min(foods, key=protein_food), max(foods, key=protein_food))
print(proteins)

calories = (min(foods, key=calories_food), max(foods, key=calories_food))
print(calories)

# refactor selecting foods to use lambda functions
min_max_protein = (
    min(foods, key=lambda item: item["protein"]),
    max(foods, key=lambda item: item["protein"]),
)
print(min_max_protein)

# reformat the foods into [ food: {calories: c, protein: p}, ... ]

foods_list = [
    {"name": "strawberries", "calories": 33, "protein": 0.7},
    {"name": "waffles", "calories": 291, "protein": 8},
    {"name": "eggs", "calories": 155, "protein": 13},
    {"name": "chicken breast", "calories": 165, "protein": 31},
]

# from fool_list, construct a food_dict
foods_dict = {item.pop("name"): item for item in foods_list}
print(foods_dict)

for key, item in foods_dict.items():
    print(key, item)

for item in foods_dict.values():
    print(item)

foods_list = [
    {"name": "strawberries", "calories": 33, "protein": 0.7},
    {"name": "waffles", "calories": 291, "protein": 8},
    {"name": "eggs", "calories": 155, "protein": 13},
    {"name": "chicken breast", "calories": 165, "protein": 31},
]

# from fool_list, construct a food_dict
foods_dict = {item.pop("name"): item for item in foods_list}
print(foods_dict)


# method calling from various classes/instances


class A:
    def methodA(self):
        print("hello from method A")


class B:
    def methodB(self):
        print("hello from method B")


a = A()
a.methodA()

b = B()
b.methodB()

# bools
print(True < False)
print(True > False)

print(True < True)

z = False and False
print(z)


# class inheritance exercise:  Pet class with subclasses
class Pet:
    sound = ""

    def __init__(self, name):
        self.name = name

    def speak(self):
        sound = self.sound
        return sound + "!"

    def describe(self):
        name = self.name
        kind_of_pet = self.__class__.__name__.lower()
        return f"{name} the {kind_of_pet} says {self.speak()}"


class Dog(Pet):
    sound = "Woof"


class LapDog(Dog):
    sound = "Yap"


# requirement:  implement code that will make the LoudLapDog say YAP!YAP!YAP!
class LoudLapDog(LapDog):
    # why doesn't the next line work alone (without defining speak)?
    #   ans: super() does not know what self is, thus it can't know what is its parent class
    # sound = super().speak().upper() * 3
    def speak(self):
        sound = super().speak().upper() * 3
        return sound


clyde = Dog("Clyde")
sap = LapDog("Sap")
sappy = LoudLapDog("Sappy")

print(clyde.describe())
print("")
print(sap.describe())
print("")
print(sappy.describe())

# counting words in a string of input
words = "beauty is truth truth beauty".split()
# counts = {}
# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1
#
# print(counts)

# another way to perform the counting process

counts = defaultdict(int)
for word in words:
    counts[word] += 1

print(counts)


def one():
    return 1


print(one)
print(one())
one_dict = defaultdict(one)
print(one_dict["k"])
print(one_dict)

# lambda function form of one
ONE = lambda: 1
print(ONE)
print(ONE())
ONE()
try:
    print(ONE())
except TypeError as error:
    print(f"TypeError: {error}")


f = lambda y: y * y + 1.1
print(f(1))

cplx_str1 = """ My favorite website is docs.python.org, with reddit.com coming in a close second."
    """
print(type(cplx_str1))
print(cplx_str1)

mystring = "my string."
print(mystring)

# another example

# regex_pattern for finding sentences
pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"


class Paragraph:
    # split_str_sentences = regex_pattern
    null_string = ""
    _words_with_period = {"a.m.", "p.m.", "Mr.", "Mrs.", "Ms."}

    def __init__(self, text):
        self.text = text

    def num_sentences(self):
        my_str = self.text
        for wrd in self._words_with_period:
            all_words = re.findall(wrd, my_str)
            if all_words:
                print(all_words)
                my_str = my_str.replace(wrd, "#####")
                # all_words = []
        print(my_str)
        split_string = re.split(pattern, my_str)
        if self.null_string not in split_string:
            pass
        else:
            split_string.pop(split_string.index(""))
        count = len(split_string)
        return count


string2 = """Mr. Smith bought cheap_site.com for 1.5 million dollars, 
i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true...
 Well, with a probability of .98, it isn't!
"""

cplx_str = """Did you tell Mr. Burke yesterday before 9 p.m.? Mrs. Burke and Ms. Edwards are bringing the
birthday cake tomorrow at approximately 10 a.m."""

wrd = "Mr."
find_str = re.findall(wrd, cplx_str)
print(find_str)
t_str = cplx_str.replace(wrd, "#####")
print(t_str)

print(cplx_str)

par_count = Paragraph(cplx_str).num_sentences()
print(par_count)

# t_str = cplx_str
# for word in _words_with_period:
#     all_words = re.findall(word, t_str)
#     if all_words:
#         print(all_words)
#         t_str = t_str.replace(word, "###")
#         all_words = []
# print(t_str)
