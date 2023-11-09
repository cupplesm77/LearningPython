# misc.py

from collections import defaultdict


CACHE_SIZE = 2
def memoize(func):
    cache = {}
    keys = defaultdict(list)

    def wrapper(*args, **kwargs):
        key = args

        if len(cache) < CACHE_SIZE:
            if key not in cache:
                cache[key] = func(*args, **kwargs)

        elif len(cache) == CACHE_SIZE:
            if key not in cache:
                last_key = keys["keys"][-1]
                for ckey in cache.keys():
                    if ckey != last_key:
                        save_key = ckey
                cache.pop(save_key)
                cache[key] = func(*args, **kwargs)

        keys["keys"].append(key)
        return cache[key]

    return wrapper


@memoize
def f(x):
    print(f"CALLING: f {x}")
    return x ** 2

print(f(2))
# CALLING: f 2
# 4
print(f(2))
# 4
print(f(7))
# CALLING: f 7
# 49
print(f(7))
# 49
print(f(9))
# CALLING: f 9
# 81
print(f(9))
# 81
print(f(7))
# 49
print(f(2))
# CALLING: f 2
# 4

print("")
@memoize
def g(x, y):
    print(f"CALLING: g {x} {y}")
    return (2 - x) / y


print(g(-6, 2))
# CALLING: g -6 2
# 4.0
print(g(-6, 2))
# 4.0
print(g(-6, 2))
# 4.0
print(g(6, 2))
# CALLING: g 6 2
# -2.0
print(g(6, 2))
# -2.0
print(g(-6, 2))
# 4.0
test1 = g(12, -2)
print(test1)
# CALLING: g 12 -2
# 5.0
print(g(12, -2))
# 5.0
test2 = g(-6, 2)
print(test2)
# 4.0
print(g(6, 2))
# CALLING: g 6 2
# -2.0