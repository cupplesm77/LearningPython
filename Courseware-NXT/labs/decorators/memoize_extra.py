'''
>>> f(2)
CALLING: f 2
4
>>> f(2)
4
>>> f(7)
CALLING: f 7
49
>>> f(7)
49
>>> f(9)
CALLING: f 9
81
>>> f(9)
81
>>> f(7)
49
>>> f(2)
CALLING: f 2
4


>>> g(-6, 2)
CALLING: g -6 2
4.0
>>> g(-6, 2)
4.0
>>> g(-6, 2)
4.0
>>> g(6, 2)
CALLING: g 6 2
-2.0
>>> g(6, 2)
-2.0
>>> g(-6, 2)
4.0
>>> g(12, -2)
CALLING: g 12 -2
5.0
>>> g(12, -2)
5.0
>>> g(-6, 2)
4.0
>>> g(6, 2)
CALLING: g 6 2
-2.0


>>> h(2, 4)
CALLING: h 2 4 42
7
>>> h(2, 4)
7
>>> h(3, 2, z=31)
CALLING: h 3 2 31
6
>>> h(3, 2, z=31)
6
>>> h(2, 4)
7
>>> h(1, 1, z=-2)
CALLING: h 1 1 -2
-1
>>> h(3, 2, z=31)
CALLING: h 3 2 31
6

'''


# Implement a memoize decorator that saves up to the two most recent
# calls.  (I.e., an LRU cache with max size of 2.)
# HINT: While not necessary, it may help to use the collections module.

# Write your code here:
from collections import defaultdict


CACHE_SIZE = 2
def memoize(func):
    cache = {}
    keys = defaultdict(list)

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if len(cache) < CACHE_SIZE:
            if key not in cache:
                cache[key] = func(*args, **kwargs)

        elif len(cache) == CACHE_SIZE:
            if key not in cache:
                last_key = keys["keys"][-1]
                for ckey in cache.keys():
                    if ckey != last_key:
                        pop_key = ckey
                cache.pop(pop_key, None)
                cache[key] = func(*args, **kwargs)

        keys["keys"].append(key)
        return cache[key]

    return wrapper


# Do not edit any code below this line!

@memoize
def f(x):
    print(f"CALLING: f {x}")
    return x ** 2


@memoize
def g(x, y):
    print(f"CALLING: g {x} {y}")
    return (2 - x) / y


@memoize
def h(x, y, z=42):
    print(f"CALLING: h {x} {y} {z}")
    return z // (x + y)


if __name__ == '__main__':
    import doctest

    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python. Copyright MigrateUp LLC. All rights reserved.
