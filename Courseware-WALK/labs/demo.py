# demo.py

import numpy

# run with and without python -O option : python -O .\demo.py  and python .\demo.py

# demonstrate output usage of f-string {param = } format

x = '12'
print(f"x = {x}")
print(f"{x = }")



# showing __debug__ values with and without -O option
print(f"__debug__ = {__debug__}")
print(f"{__debug__ = }")
print(f"{__name__ = }")
print(f"__name__ = {__name__}")

if __debug__:
    print("Running in Normal mode!")
else:
    print("Running in Optimized mode!")


# Best practice
def square(x):
    if x < 0:
        raise ValueError(" ValueError in function 'square': only positive numbers are allowed")
    return x ** 2

try:
    square(-2)
except ValueError as error:
    print(error)

print("That's all folks")
