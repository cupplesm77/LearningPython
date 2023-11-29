# misc2.py

from collections import defaultdict



d = {}


print(d)

NOTHERE = object()


def afunction():
    pass

def add(arg_add):
    def decorator(func):
        def wrapper(*args, **kwargs):
            fx = func(*args, **kwargs) + arg_add
            return fx

        return wrapper

    return decorator

@add(2)
def g(x):
    return x ** 2

print(g(2))
print(g(10))

g = NOTHERE

r = NOTHERE

print(g is r)

def plus5(func):
    def wrapper(*arg, **kwargs):
        f = func(*arg, **kwargs) + 5
        return f

    return wrapper


@plus5
def f(x):
    return x


print(f(2))


class Horse:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


p = Horse('Pinto')
s = Horse('Shire')
p.add_trick('prance')
s.add_trick('gallop')
print(p.tricks)
print(s.tricks)

print(p.name)
print(s.name)
del p.name
print(p.name)


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
# ['roll over']
print(e.tricks)
# ['play dead']


mlist = [0, 1, 2, 3, 4, 5]
mlist.insert(0, 100)
pos = mlist.index(3)
mlist.pop(pos)
print(mlist)
print("")


def func(x, y):
    return x + y


keys = [(1, 3), (0, 5), (4, 1), (1, 3), (2, 33), (2, 33)]
# values = [12, 1, 7, 12, 8, 9]
cache = {}
order = []
for key in keys:
    if key in cache:
        pos = order.index(key)
        order.pop(pos)
    else:
        cache[key] = func(key[0], key[1])
    order.insert(0, key)
    print(f"key = {key}")
    print(f"cache = {cache}")
    print(f"order = {order}")

# create a dictionary from mlist and keys
new_dict = dict(zip(keys, mlist))
print(new_dict)
y = new_dict.get((2, 33), "NOUGHT")
print(y)
