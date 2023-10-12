"""
>>> evens = evens_up_to(8)
>>> type(evens)
<class 'generator'>
>>> for even in evens:
...     print(even)
2
4
6
8

>>> squares = squares_up_to(16)
>>> type(squares)
<class 'generator'>
>>> for square in squares:
...     print(square)
1
4
9
16

>>> for square in squares_up_to(15):
...     print(square)
1
4
9

>>> counter = countdown(3)
>>> type(counter)
<class 'generator'>
>>> for count in countdown(3):
...     print(count)
3
2
1
BLASTOFF!

>>> for count in countdown(10):
...     print(count)
10
9
8
7
6
5
4
3
2
1
BLASTOFF!

"""


# Write your code here:


def evens_up_to(num):
    for n in range(2, num + 1, 2):
        yield n


def squares_up_to(max_square):
    number = 1
    while True:
        square = number * number
        if square > max_square:
            return
        yield square
        number += 1


def countdown(from_num):
    for n in range(from_num, 0, -1):
        yield n
    yield "BLASTOFF!"


evens = evens_up_to(8)
print(type(evens))
# <class 'generator'>
for even in evens:
    print(even)

squares = squares_up_to(16)
print(type(squares))
# <class 'generator'>
for square in squares:
    print(square)

counter = countdown(3)
print(type(counter))
# <class 'generator'>
for count in countdown(3):
    print(count)

for count in countdown(10):
    print(count)

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest

    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
