# misc.py

dict = [{'a': 1, 'ab': 12, 'AAAAAAA': 7, 'cdf': 3},
                {'a': 2, 'ab': -20, 'AAAAAAA': 19, 'cdf': 2},
                {'a': 3, 'ab': 2, 'AAAAAAA': 9, 'cdf': 1},
                ]

l_str = ["12", "4", "-7", "21", "-33", "7"]

l_int = [12, -4, 7, 21, -33, 7]

def get_ab(student):
    return student["ab"]

def max_func(items, key=None):
    biggest = items[0]

    # case of no key and no func
    if key is None:
        for item in items[1:]:
                if item > biggest:
                    biggest = item
    else:
        for item in items[1:]:
            if key(item) > key(biggest):
                    biggest = item

    return biggest

max_ab = max_func(dict, key=get_ab)
print(max_ab)

max_str = max_func(l_str, key=int)
print(max_str)

max_str = max_func(l_int, key=abs)
print(max_str)
