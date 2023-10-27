# varargs1.py
'''
Python uses * and ** for two very different things:

   * Variable arguments (when defining a function)
   * Argument unpacking (when calling a function)
'''

def print_args(*args):
    for arg in args:
        print(arg)


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} -> {value}")


def print_all(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} -> {value}")


def add_to_dict(stuff, *args, **kwargs):
    for key, value in kwargs.items():
        if key not in stuff:
            stuff[key] = value

    return stuff


def normal_function(a, b, c):
    print(f"a: {a} b: {b} c: {c}")


numbers = (3, 2, 1)

normal_function(*numbers)

other_numbers = {'a': 1, 'b': 1, 'c': 1}

normal_function(**other_numbers)


def another_normal_function(a, b, c=1, d=2, e=300):
    return a + b + c + d + e


nums = (3, 5)
extras = {'d': 5, 'e': 2}
print(another_normal_function(*nums, **extras))


def order_book(title, author, isbn):
    """

    :param title:
    :param author:
    :param isbn:
    :return:
    """
    print(f'Ordering "{title}" by {author} ({isbn})')


def get_required_textbook(class_id):
    """

    :param class_id:
    :return:
    """
    return "Coloring with Great Enthusiasm", "Joseph Nash", 22447788


book = get_required_textbook(4242)
print(book)
order_book(*book)

print_args('red', 'blue', 'green')
print("")
print_args()
print('')
print_args(' ')
print('')
print_kwargs(x=4, y=10)
print('')
print_all(4, 5, 6, z=15, x='test')
print_all(4, 5)
print_all(x='test2', y=0.99)
print('')
print(add_to_dict({}, 2, 3, x=10, y='test3'))
