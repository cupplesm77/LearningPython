'''Let's play with the different ways to use variable arguments in
Python.  Define the functions below to make everything pass.

>>> values = {"a":3, "b":2, "c":4}
>>> some_values = {"c": 7, "b": 4}

>>> product(2, 7, 3)
42
>>> product(**values)
24
>>> product(1, **some_values)
28

>>> amounts = {"u": 3, "v": 2, "w": 4}
>>> some_amounts = {"v": 7, "w": 4}
>>> total(1, 2, 3)
6
>>> total(**amounts)
9
>>> total(3, **some_amounts)
14

>>> max_even(2, 3)
2
>>> max_even(2, 4)
4
>>> max_even(2, 3, 9, 11, 7, 8, 13, 21)
8


>>> point = (3, 8, 2)
>>> coordinates = {'x': 8, 'y': 33, 'z': -4}

IMPORANT HINT: Remember that * and ** are used for two different
things: when _calling_ a function (argument unpacking), and when
_defining_ a function (varargs).

>>> set_destination(*point)
Going to x=3, y=8, z=2

>>> set_destination(**coordinates)
Going to x=8, y=33, z=-4

'''


# Write your code here:
def product(*args, **kwargs):
    prod = 1
    if args:
        for arg in args:
            prod *= arg
    if kwargs:
        for key, value in kwargs.items():
            prod *= value
    return prod


def total(*args, **kwargs):
    sum = 0
    if args:
        for arg in args:
            sum += arg
    if kwargs:
        for key, value in kwargs.items():
            sum += value
    return sum


def max_even(*args):
    return max([x for x in args if x%2 == 0])


# IMPORANT HINT: Remember that * and ** are used for two different
# things: when _calling_ a function (argument unpacking), and when
# _defining_ a function (varargs).
def set_destination(*args, **kwargs):
    if args:
        print(f"Going to x={args[0]}, y={args[1]}, z={args[2]}")

    if kwargs:
        v = []
        for value in kwargs.values():
            v.append(value)
        print(f"Going to x={v[0]}, y={v[1]}, z={v[2]}")


if __name__ == '__main__':
    import doctest

    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python. Copyright MigrateUp LLC. All rights reserved.
