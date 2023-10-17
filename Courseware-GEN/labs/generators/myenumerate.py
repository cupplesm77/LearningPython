# myenumerate.py

# from _collections_abc import Generator

# here is how enumerate works
pets = ["goat", "frog", "turtle"]
enum1 = enumerate(pets)
print(type(enum1))
for idx, p in enum1:
    print(idx, p)


class myenumerate():
    def __init__(self, container):
        if not isinstance(container, list) and not isinstance(container, set):
           raise TypeError("input must be a list or a set")
        range_container = range(len(container))
        self._enum_container = list(zip(range_container, container))

    def __iter__(self):
        return self

    def __next__(self):
        value = self._enum_container.pop(0)
        return value


pets_set = set(pets)
enum_list = myenumerate(pets_set)
print(type(enum_list))
for i in range(len(pets_set)):
    print(next(enum_list))

