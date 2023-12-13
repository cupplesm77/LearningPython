'''

>>> colors = ['Brick Red', 'Fern Green',
...    'Deep Sky Blue', 'Cadmium Orange']

Implement get_index_or_default() by catching an exception.

>>> get_index_or_default(colors, 0, 'Burgundy')
'Brick Red'
>>> get_index_or_default(colors, 10, 'Burgundy')
'Burgundy'
>>> get_index_or_default(colors, -1, 'Bright Pink')
'Cadmium Orange'
>>> get_index_or_default(colors, 5, 'Bright Pink')
'Bright Pink'


Now implement a function to parse a string into first and last name:

>>> parsed = parse_name('John Smith')
>>> type(parsed)
<class 'dict'>
>>> parsed['first']
'John'
>>> parsed['last']
'Smith'

>>> parsed = parse_name('Melissa Jones')
>>> parsed['first']
'Melissa'
>>> parsed['last']
'Jones'

>>> parse_name('John Wayne Smith')
Traceback (most recent call last):
...
ValueError: Cannot split name: John Wayne Smith

>>> parse_name('Bob')
Traceback (most recent call last):
...
ValueError: Cannot split name: Bob


And another function to parse a USA-style phone number.

>>> parts = parse_phone_number('415-555-1212')
>>> type(parts)
<class 'dict'>
>>> parts['area']
'415'
>>> parts['exchange']
'555'
>>> parts['last4']
'1212'


>>> parts = parse_phone_number('303-777-1234')
>>> parts['area']
'303'
>>> parts['exchange']
'777'
>>> parts['last4']
'1234'

>>> parse_phone_number('415-555-12345')
Traceback (most recent call last):
...
ValueError: Invalid format: 415-555-12345

>>> parse_phone_number('41-555-1234')
Traceback (most recent call last):
...
ValueError: Invalid format: 41-555-1234

>>> parse_phone_number('415-55-1234')
Traceback (most recent call last):
...
ValueError: Invalid format: 415-55-1234

>>> parse_phone_number('415-555')
Traceback (most recent call last):
...
ValueError: Invalid format: 415-555

'''

# Write your code here:
def get_index_or_default(color_array, index, default_color):
    try:
        color = color_array[index]
    except IndexError:
        return default_color
    return color

def parse_name(name):
    name_types = ['first', 'last']
    names = name.split(" ")
    if len(names) != 2:
        raise ValueError("Cannot split name: " + str(name))

    return dict(zip(name_types, names))


def parse_phone_number(phone_number):
    number_types = ['area', 'exchange', 'last4']
    phone_numbers = phone_number.split("-")

    if len(phone_numbers) != 3:
        raise ValueError("Invalid format: {}".format(phone_number))

    area_len = len([c for c in phone_numbers[0]])
    if area_len != 3:
        raise ValueError("Invalid format: {}".format(phone_number))

    exchange_len = len([c for c in phone_numbers[1]])
    if exchange_len != 3:
        raise ValueError("Invalid format: {}".format(phone_number))

    last4_len = len([c for c in phone_numbers[2]])
    if last4_len != 4:
        raise ValueError("Invalid format: {}".format(phone_number))

    phone_number_zip = zip(number_types, phone_numbers)
    phone_number_dict = dict(phone_number_zip)
    return phone_number_dict


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python. Copyright MigrateUp LLC. All rights reserved.
