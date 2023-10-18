# myrange.py

from enum import Enum

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


#
# test = myrange(3, -2, -1)
# print(next(test))

# tst_1_myrange = tst_myrange(1, 10, 2)
# print(tst_1_myrange)
#
# tst_2_myrange = tst_myrange(1, 6)
# print(tst_2_myrange)
#
# tst_3_myrange = tst_myrange(5)
# print(tst_3_myrange)


# number = myrange(0, 10, 2)
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))

# myrange(1, 2, 1)
#
# for num in myrange(1, 5, 1, 1):
#     print(num)
#
# myrange(1, 4)
#
# for b in myrange(10):
#     print(b)

#
# a = myrange(2, 1)
# next(a)
#
# for r in myrange(1, 2, 3, 4):
#     print(r)

# testing range builtin
# for num in range(-4, -2, 2):
#     print(num)
