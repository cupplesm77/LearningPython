'''In this lab, you practice "fanning in" and "fanning out" with generator functions.

NOTE: The methods of str are detailed here:
https://docs.python.org/3/library/stdtypes.html#string-methods

First, define the words_in_text() generator function. It takes a path
to a text file, and reads its contents, producing its words one at a
time.

Start with a simple file, "poem-simple.txt" in this directory:

>>> words = words_in_text(fullpath("poem-simple.txt"))
>>> type(words)
<class 'generator'>
>>> for word in words:
...     print(word)
all
night
our
room
was
outer-walled
with
rain
drops
fell
and
flattened
on
the
tin
roof
and
rang
like
little
disks
of
metal



Next, write a generator function called book_records(), which also
takes a file path - specifically, "book-data-simple.txt" in this
directory. Look in this file, and you'll find it has book records
spread across different lines, with a blank line between each record.

>>> books = book_records(fullpath("book-data-simple.txt"))
>>> type(books)
<class 'generator'>

>>> book = next(books)
>>> book['title']
'Ordinary Grace'
>>> book['author']
'William Kent Krueger'
>>> book['isbn']
'1451645856'

>>> book = next(books)
>>> book['title']
'A Faithful Son'
>>> book['author']
'Michael Scott Garvin'
>>> book['isbn']
'1519414730'

>>> book = next(books)
>>> book['title']
'The Legacy of Lucy Harte'
>>> book['author']
'Emma Heatherington'
>>> book['isbn']
'0008194866'

>>> book = next(books)
Traceback (most recent call last):
...
StopIteration


Those are the simpler cases - now let's handle more complex
situations.  First, go back to words_in_text(), and extend it to
handle punctuation, and lowercasing any capital letters. These are in
"poem-full.txt":

>>> for word in words_in_text(fullpath("poem-full.txt")):
...     print(word)
all
night
our
room
was
outer-walled
with
rain
drops
fell
and
flattened
on
the
tin
roof
and
rang
like
little
disks
of
metal



Next, extend books_records() to handle more complex records. That's in
"book-data-complex.txt":

>>> books = book_records(fullpath("book-data-complex.txt"))
>>> book = next(books)
>>> book['title']
'First and Only: A psychological thriller'
>>> book['author']
'Peter Flannery'
>>> book['isbn']
'0957091907'
>>> book['price']
9.57

>>> book = next(books)
>>> book['title']
'A Man Called Ove'
>>> book['author']
'Fredrik Backman'
>>> 'isbn' in book
False
>>> 'price' in book
False

>>> book = next(books)
>>> book['title']
"A Dog's Purpose: A Novel for Humans"
>>> book['author']
'W. Bruce Cameron'
>>> book['isbn']
'0765330342'
>>> book['price']
8.92

>>> book = next(books)
Traceback (most recent call last):
...
StopIteration

'''

from os.path import dirname, join

this_directory = dirname(__file__)

import re


def fullpath(filename):
    '''Returns the full path of a file in this directory. Allows you to
    run the lab easily in an IDE, or from a different working directory.
    '''
    return join(this_directory, filename)


# Write your code here:

def words_in_text(path):
    with open(path) as handle:
        for line in handle:  # note that the "handle" could be very long...potential bottleneck
            line = line.rstrip("\n").lower()
            line = re.sub(r"[.!?,]", "", line)
            for word in line.split():
                yield word


def book_records(path):
    with open(path) as lines:
        record = {}
        for line in lines:
            if line == '\n':
                yield record
                record = {}
                continue
            key, value = line.rstrip('\n').split(': ', 1)
            if key == 'price':
                value = float(value)
            record[key] = value
        yield record


words = words_in_text(fullpath("poem-simple.txt"))
print(type(words))
# <class 'generator'>
for word in words:
    print(word)

books = book_records(fullpath("book-data-simple.txt"))
print(type(books))
# <class 'generator'>

book = next(books)
print(book['title'])
# 'Ordinary Grace'
print(book['author'])
# 'William Kent Krueger'
print(book['isbn'])
# '1451645856'

book = next(books)
print(book['title'])
# 'A Faithful Son'
print(book['author'])
# 'Michael Scott Garvin'
print(book['isbn'])
# '1519414730'

book = next(books)
book['title']
# 'The Legacy of Lucy Harte'
book['author']
# 'Emma Heatherington'
book['isbn']
# '0008194866'
# book = next(books)

for word in words_in_text(fullpath("poem-full.txt")):
    print(word)

books = book_records(fullpath("book-data-complex.txt"))
book = next(books)
print(book['title'])
# 'First and Only: A psychological thriller'
print(book['author'])
# 'Peter Flannery'
print(book['isbn'])
# '0957091907'
print(book['price'])
# 9.57

book = next(books)
print(book['title'])
# 'A Man Called Ove'
print(book['author'])
# 'Fredrik Backman'
print('isbn' in book)
# False
print('price' in book)
# False

book = next(books)
print(book['title'])
# "A Dog's Purpose: A Novel for Humans"
print(book['author'])

# 'W. Bruce Cameron'
print(book['isbn'])
# '0765330342'
print(book['price'])
# 8.92
# book = next(books)


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest

    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
