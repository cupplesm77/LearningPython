# misc.py

from collections import defaultdict

# Version using lists
MAX_SIZE = 3
def memoize(func):
    cache = {}
    order = []
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            pos = order.index(key)
            order.pop(pos)
        else:
            cache[key] = func(*args, **kwargs)
        order.insert(0, key)
        while len(order) > MAX_SIZE:
            old_key = order.pop()
            del cache[old_key]
        return cache[key]
    return wrapper

CACHE_SIZE = 2
def memoize2(func):
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

@memoize
def g(x, y):
    print(f"CALLING: g {x} {y}")
    return (2 - x) / y

@memoize
def h(x, y, z=42):
    print(f"CALLING: h {x} {y} {z}")
    return z // (x + y)

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

print("")

print(h(2, 4))
# CALLING: h 2 4 42
# 7
print(h(2, 4))
# 7
print(h(3, 2, z=31))
# CALLING: h 3 2 31
# 6
print(h(3, 2, z=31))
# 6
print(h(2, 4))
# 7
print(h(1, 1, z=-2))
# CALLING: h 1 1 -2
# -1
print(h(3, 2, z=31))
# CALLING: h 3 2 31
# 6