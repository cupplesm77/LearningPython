# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 12:32:26 2023

@author: gravi
"""

# misc
message = None
if message:
    print(f'message = {message}')


# dictionary comprehension
def test():
    print('Joe was here!')


channels = ['lunch', 'dinner']
# initialize a dictionary of empty dictionaries for each channel
channel_dict = {channel: dict() for channel in channels}
print(channel_dict)
callback = test
channel = 'lunch'
who = 'Joe'
subscribers = channel_dict[channel]
subscribers[who] = callback
print(channel_dict)

x = {'a': {}, 'b': {}}
z = x
print(id(x))
print(id(z))
print(type(x['b']))
y = x['b']
print(type(y))
y['c'] = 14
print(x)
y['d'] = 44
print(x)
del y['c']
print(x)

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
b.append(10)
print(b)
print(a)

# xml generator
kwargs = {'a': 1, 'b': 2, 'c': 3}
''.join(kwargs)
mylist = [f' {key}="{value}"'
          for key, value in kwargs.items()]
mylist_joined = ''.join(mylist)
print(type(mylist_joined))
print(len(mylist_joined))
print(mylist_joined)


def mxml(tag, content='', **parameters):
    attrs = ''.join([f' {key}="{value}"'
                     for key, value in parameters.items()])
    return f'<{tag}{attrs}>{content}</{tag}>'


print(mxml('body', 'My Praise to God', a=1, b=2, c=3))


# two_times example
def two_times(func):
    def wrapper(*args):
        times2 = func(*args) * 2
        return times2

    return wrapper


@two_times
def f(num1, num2):
    return num1 * num2


z = f(2, 3)
print(z)

# length of a string
s = 'The boy ran to the nearest home'
print(len(s))

import os
path = 'watched_file.txt'
step = 0
with open(path, 'r') as file:
    first_position = file.tell()
    content = file.read()
    filesize0 = len(content)
    print(filesize0)
    print('')
    file_size_bytes = os.stat(path).st_size
   # byte_length_file = bytes(content, 'utf-8')
    print(f'file of size {filesize0} characters contains {file_size_bytes} bytes')



