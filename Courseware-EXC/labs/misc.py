# misc.py

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