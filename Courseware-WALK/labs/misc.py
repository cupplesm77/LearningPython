# misc.py

d = {
    "one": 1,
    "Two": 2,
    "three": 3,
    "ten": 10,
}

print(d)
d.pop('ten')
print(d)
print("")

key = []
for item in d:
    key.append(item)
print(key)
print("")

for item in key:
    if item == "Two":
        d['two'] = d[item]
        d.pop("Two")

print(d)