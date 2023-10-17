# myenumerate.py

# # here is how enumerate works
pets = ["goat", "frog", "turtle"]
# enum1 = enumerate(pets)
# print(type(enum1))
# for idx, p in enum1:
#     print(idx, p)


def myenumerate(container, *arg):

    if not isinstance(container, list) and not isinstance(container, set):
        raise TypeError("input must be a list or a set")

    if len(arg) == 0:
        start = 0
        end = len(container)
    else:
        start = arg[0]
        end = len(container) + arg[0]
    range_container = range(start, end)
    enum_container = list(zip(range_container, container))
    for x in enum_container:
        yield x


pets_set = set(pets)
enum_list = myenumerate(pets_set, 1)
print(type(enum_list))
for idx in range(len(pets_set)):
    print(next(enum_list))
