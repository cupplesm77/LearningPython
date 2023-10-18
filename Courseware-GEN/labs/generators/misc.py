# misc.py
from myrange import myrange



# f_obj = range(1, 10, 1, 2)
f_obj = range()
print(next(f_obj))

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

    if numArgs == ONE:     # myrange has one argument
        start = ZERO
        end = args[ZERO]
        step = ONE
    elif numArgs == TWO:   # myrange has two arguments
        start = args[ZERO]
        end = args[ONE]
        step = 1
    elif numArgs == THREE:   # myrange has three arguments
        start = args[ZERO]
        end = args[ONE]
        step = args[TWO]
    else:                 # myrange has greater than three arguments
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


for n in myrange(11, -4, -2):
    print(n)


for n in myrange(12.8, 40, 1):
    print(n)

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
