# misc2.py
from itertools import combinations
import numpy as np
import pandas as pd
import numpy as np

l = [x for x in range(10)]
print(type(l))
for lx in l:
    print(lx)
l_iter = iter(l)
print(type(l_iter))
next(l_iter)
next(l_iter)
next(l_iter)
for ly in l_iter:
    print(ly)
for ly in l_iter:
    print(ly)
# next(l_iter)

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df)

d = {'col1': ['a'], 'col2': [5]}
df = pd.DataFrame(data=d)
print(df)

mdict = {'Temperature': [3068, 4112],
         'L': [0.002, 0.003],
         'R': [0.17, 0.18],
         'A_M': [16.12, 17.1],
         'Color': ["Red", "Orange"],
         "Spectral_Class": ["M", "M"],
         'Type': [0, 0]
         }

print(mdict)

df = pd.DataFrame(data=mdict)

print(df)

for irows, row in df.iterrows():
    print(row, '\n')


languages = ['Python', 'R', 'SQL', 'Julia']
programmers = combinations(languages, 2)
print(*programmers)


record = {}
string = 'Address: 122 North Ave.'
key, value = string.rstrip('\n').split(': ', 1)
record[key] = value
print(record)

def myrange(*args):
    """

    :param args: int
    :return: int
    """
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3

    # error checking on the args
    numArgs = len(args)
    # ValueErrors
    if numArgs == ZERO:
        raise TypeError(f"myrange expected at least 1 argument, got {numArgs}")
    if numArgs > THREE:
        raise TypeError(f"myrange expected at most 3 arguments, got {numArgs}")
    if numArgs == TWO and args[ZERO] > args[ONE]:
        raise ValueError(f"'start' cannot be greater than 'end': myrange args are {args}")
    if numArgs == THREE and args[TWO] > ZERO and args[ZERO] > args[ONE]:
        raise ValueError(f"For counting up, 'start' cannot be greater than 'end': myrange args are {args}")
    if numArgs == THREE and args[TWO] < ZERO and args[ONE] > args[ZERO]:
        raise ValueError(f"For counting down, 'start' cannot be less than 'end': myrange args are {args}")
    # TypeErrors
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError(f"myrange arguments must be type int: myrange args are {args}")

    # set up the start, stop, and step values for the "myrange" function

    if numArgs == ONE:  # myrange has one argument
        start = ZERO
        end = args[ZERO]
        step = ONE
    elif numArgs == TWO:  # myrange has two arguments
        start = args[ZERO]
        end = args[ONE]
        step = ONE
    elif numArgs == THREE:  # myrange has three arguments
        start = args[ZERO]
        end = args[ONE]
        step = args[TWO]
    else:  # myrange has greater than three arguments
        return "myrange generator function has more than three args"

    # counting up from a start value to an "end" value
    if step > ZERO:
        n = start
        while n < end:
            yield n
            n += step

    # counting down from a start value to an end value
    if step < ZERO:
        n = start
        while n > end:
            yield n
            n += step


gen_obj = iter(myrange(2, 7, 1))
print(next(gen_obj))
g = lambda: next(gen_obj)
print(g())
for x in gen_obj:
    print(x)
# print(next(gen_obj))

# in the range example below, the gen_obj1 see an exception upon formation:
# gen_obj1 = range(1, 2, 1, 1)
# C:\Users\gravi\Powerful_Python\Courseware-GEN\venv\Scripts\python.exe C:\Users\gravi\Powerful_Python\Courseware-GEN\labs\generators\misc2.py
# Traceback (most recent call last):
#   File "C:\Users\gravi\Powerful_Python\Courseware-GEN\labs\generators\misc2.py", line 65, in <module>
#     gen_obj1 = range(1, 2, 1, 1)
# TypeError: range expected at most 3 arguments, got 4
# print(type(gen_obj1))

x = range(10)
print(type(x))
# print(next(x))

# myrange function does not raise an exception until it reaches the next(gen_obj2) line
myrange(1, 2, 1)
gen_obj2 = myrange(1, 3, 1)
print(type(gen_obj2))
print(gen_obj2)
# here is where the TypeError exception is raised:
num = next(gen_obj2)
print(num)
# never reaches the next line for this example argument list
num = next(gen_obj2)
print(num)

mdict = {'Temperature': [3068, 4112],
         'L': [0.002, 0.003],
         'R': [0.17, 0.18],
         'A_M': [16.12, 17.1],
         'Color': ["Red", "Orange"],
         "Spectral_Class": ["M", "M"],
         'Type': [0, 0]
         }

# views of a dictionary  :  separate but tied to a dictionary
print(type(mdict))
print(type(mdict.items()))
for param, value in mdict.items():
    print(f"{param}: {value}")
for key in mdict.keys():
    print(f"key: {key}")
for value in mdict.values():
    print(f"value: {value}")


car = {'Year of Launch': [1999, np.nan, 1986, 2020, np.nan,
                          1991, 2007, 2011, 2001, 2017],
       'Engine Number': [0.0, 15, 22, 43, 44, 0.0,
                         55, 0.0, 57, np.nan],
       'Chasis Unique Id': [4023, np.nan, 3115, 4522, 3643,
                            3774, 2955, np.nan, 3587, np.nan]}

# Create the dataframe
df = pd.DataFrame(car, columns=['Year of Launch', 'Engine Number',
                                'Chasis Unique Id'])
print(df)
df_filter = df['Engine Number'].isnull()
print(df[df_filter])

for irow, row in df.iterrows():
    if row['Engine Number'] == 0.0:
        row['Year of Launch'] = 0.0

print(df)

df['Engine Number'] = df['Engine Number'][df_filter].apply(lambda x: 0.0)
print(df)

df.dropna(subset=['Chasis Unique Id'], inplace=True)

print(df)

y = range(10)
for x in y:
    print(x)
f = lambda x: 0
xlist = [f(x) for x in y]
print(xlist)