
# misc.py

class BadValueError(Exception):
    def __init__(self, val):
        self.val = val
    def describe(self):
        print(f"Really Bad Value Passed: {self.val}")

value = ["test", 44, "51", 'forty']

for val in value:
    try:
        intvalue = int(val)
        print("")
        print(intvalue)
    except ValueError as err:
        print("")
        print(f"Bad Bad Value: {err}")

import re

value = ["test4", "44", "51", 'forty']
for val in value:
    if re.match("-?\d+$", val):
        print(val)

def make_an_int(value):
    if not re.match("-?\d+$", val):
        raise BadValueError(val)

print("")
for val in value:
    try:
        make_an_int(val)
    except BadValueError as err:
        print("")
        print(f"BadValueError: {err.describe()}")

def parse_name(name):
    name_types = ['first', 'last']
    names = name.split(" ")
    if len(names) != 2:
        raise ValueError("Cannot split name: " + str(name))

    names_zip = zip(name_types, names)
    names_dict = dict(names_zip)
    return names_dict

def parse_phone_number(phone_number):
    number_types = ['area', 'exchange', 'last4']
    phone_numbers = phone_number.split("-")

    if len(phone_numbers) != 3:
        raise ValueError("Invalid format: {}".format(phone_number))

    last4_len = len([c for c in phone_numbers[2]])
    if last4_len != 4:
        raise ValueError("Invalid format: {}".format(phone_number))

    phone_number_zip = zip(number_types, phone_numbers)
    phone_number_dict = dict(phone_number_zip)
    return phone_number_dict


print(parse_name("John Smith"))
# print(parse_name("Smith"))
# print(parse_name("John Wayne Smith"))

print(parse_phone_number("222-222-22223"))

