# misc2.py

consonants = "bcdfghjklmnpqrstvwxyz" + "bcdfghjklmnpqrstvwxyz".upper()
print(consonants)

xstring = 'xyz rmw, zabcccc'
for e in xstring:
    print(e)

one_line_poems = [
    "The dogs are barking at the stillness, the stillness is still.",
    "In the canopy of the night heaven the stars are tiptoeing.",
    "A sunrise smiles wide into my expectant face.",
    "The bees are awakening to the life in a yellow wonder!",
    "The land runs astoundingly under my soles.",
    "The dance of the flowers kissed by the butterflies.",
]

def sorted_by_word_count(xlist):
    def num_words(x):
        return len(x.split())
    sorted_list = sorted(xlist, key=num_words)
    return sorted_list

print(sorted_by_word_count(one_line_poems))

for poem in sorted_by_word_count(one_line_poems):
    print(poem)
# The land runs astoundingly under my soles.
# A sunrise smiles wide into my expectant face.
# The dance of the flowers kissed by the butterflies.
# The dogs are barking at the stillness, the stillness is still.
# In the canopy of the night heaven the stars are tiptoeing.
# The bees are awakening to the life in a yellow wonder!

def fewest_vowels(xstr):
    def num_vowels(x):
        vowels = "aeiouAEIOU"
        return len([y for y in x if y in vowels])

    return min(xstr, key=num_vowels)


print(fewest_vowels(one_line_poems))
# 'The land runs astoundingly under my soles.'

def most_consonants(ystr):
    def num_consonants(x):
        consonants = "bcdfghjklmnpqrstvwxyz" + "bcdfghjklmnpqrstvwxyz".upper()
        return len([y for y in x if y in consonants])
    return max(ystr, key=num_consonants)

print(most_consonants(one_line_poems))
'The dogs are barking at the stillness, the stillness is still.'


# count the number of spaces in a string
xstr = "a b c"
count = xstr.count(" ")
print(count)

xlist = ["a", "a b", "a b c", "c", "ab cd ef ghi jk", "abc"]


def most_spaces(x):
    def num_spaces(xstr):
        return xstr.count(" ")

    max_spaces = max(x, key=num_spaces)
    return max_spaces


print(most_spaces(xlist))


class Vertebrate:
    y = 'Vertebrate'

    def print_type(self):
        self.type = Vertebrate.y
        print(self.type)


class Animal(Vertebrate):
    def __init__(self, name):
        self.name = name
        self.type = Vertebrate.y

    def print_animal(self):
        print(self.name)
        print(self.type)


vertebrate = Vertebrate()
vertebrate.print_type()
deer = Animal("Running_Deer")
deer.print_animal()
