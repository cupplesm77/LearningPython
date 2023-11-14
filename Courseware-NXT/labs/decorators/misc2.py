# misc2.py

mlist = [1,2,3,4,5]
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

