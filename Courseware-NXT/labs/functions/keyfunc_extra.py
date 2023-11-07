'''
Use max, min, and sorted along with key functions to implement the
following functions and make the tests pass.

>>> most_spaces(["a", "a b", "a b c", "c", "abc"])
'a b c'

>>> one_line_poems = [
...      "The dogs are barking at the stillness, the stillness is still.",
...      "In the canopy of the night heaven the stars are tiptoeing.",
...      "A sunrise smiles wide into my expectant face.",
...      "The bees are awakening to the life in a yellow wonder!",
...      "The land runs astoundingly under my soles.",
...      "The dance of the flowers kissed by the butterflies.",
... ]

>>> fewest_vowels(one_line_poems)
'The land runs astoundingly under my soles.'

>>> most_consonants(one_line_poems)
'The dogs are barking at the stillness, the stillness is still.'

>>> for poem in sorted_by_word_count(one_line_poems):
...     print(poem)
The land runs astoundingly under my soles.
A sunrise smiles wide into my expectant face.
The dance of the flowers kissed by the butterflies.
The dogs are barking at the stillness, the stillness is still.
In the canopy of the night heaven the stars are tiptoeing.
The bees are awakening to the life in a yellow wonder!

EXTRA CREDIT:
Once you get this lab to pass, read about lambda expressions in the
Python docs:
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions 

Modify your code to use lambda expressions instead of separately defined key functions.

'''


# Write your code here:
# def most_spaces(items):
#     def num_spaces(s):
#         return s.count(" ")
#
#     return max(items, key=num_spaces)

def most_spaces(items):
    return max(items, key=lambda x: x.count(" "))


def fewest_vowels(xlist):
    def num_vowels(x):
        vowels = "aeiouAEIOU"
        return len([y for y in x if y in vowels])

    return min(xlist, key=num_vowels)


def most_consonants(ylist):
    def num_consonants(x):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return len([y for y in x if y in consonants])

    return max(ylist, key=num_consonants)


def sorted_by_word_count(xlist):
    return sorted(xlist, key=lambda x: len(x.split()))

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest

    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python. Copyright MigrateUp LLC. All rights reserved.
