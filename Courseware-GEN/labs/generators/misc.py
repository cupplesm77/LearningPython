# misc.py
from myrange import myrange


def myitems(top):
    for x in range(top, -1, -1):
        yield x ** 2
    yield "Done!"


for item in myitems(3):
    print(item)

test = list(range(-4, 0, -1))
print(test)

gen_function = myrange(1, 4, 1, 1)
print(type(gen_function))
somethingelse = lambda: list(gen_function)
print(somethingelse())

gen_obj = range(10)
print(type(gen_obj))


def myfunc(x=0):
    return x + 1


f = myfunc
print(type(f))
print(f(10))

# f = lambda x: x + 1
# print(f(3))
# print('')
# print((lambda x: x + 1)(3))
#
# # # what does this mean?
# something = lambda: x + 1
# print(type(something))
# print(something())


# def myrange(*args):
#     # set up the start, stop, and step values for the "myrange" function
#     len_args = len(args)
#     if len_args == 1:
#         start = 0
#         end = args[0]
#         step = 1
#     elif len_args == 2:
#         start = args[0]
#         end = args[1]
#         step = 1
#     elif len_args == 3:
#         start = args[0]
#         end = args[1]
#         step = args[2]
#     else:
#         start = None
#         end = None
#         step = None
#
#     n = start
#     while n < end:
#         yield n
#         n += step

#
# r1 = myrange(3)
# print(type(r1))
# # <class 'generator'>
# for num in r1:
#     print(num)
#
#
# def pv(u):
#     print(u)
#
#
# (lambda: pv(10))()
#
# z = lambda: pv(101)
# z()
#
# pets = ["goat", "frog", "turtle"]
# z = enumerate(pets)
# print(type(z))
# for i in range(len(pets)):
#     print(next(z))
#
# container = [10, 20, 30, 40]
# for i in range(len(container)):
#     print(i)
#     print(container.pop(0))
# len_container = len(container)
# range_container = range(len_container)
# enum_container = zip(range_container, container)
# print(type(enum_container))
# print(next(enum_container))
# print(next(enum_container))
#
# # len_container = len(self._container)
# # range_container = range(len_container)
# # enum_container = zip(range_container, self._container)
# # return enum_container
#
#
# print(*enum_container)
# enum_container = zip(range_container, container)
# x, y = zip(*enum_container)
# print(x, y)
#
#
# class Fib:
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __next__(self):
#         return_value = self.a
#         self.a, self.b = self.b, self.a + self.b
#         return return_value
#
#     def __iter__(self):
#         return self
#
#
# f = Fib()
# print(type(f))
# for i in range(5):
#     print(next(f))
