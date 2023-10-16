# myrange.py

def myrange(*args):
    """

    :param args: int
    :return: int
    """
    # error checking on the args
    print(f"myrange args are {args}")
    len_args = len(args)
    # ValueErrors
    if len_args == 0:
        raise ValueError(f"myrange must have at least one argument: myrange args are {args}")
    if len_args > 3:
        raise ValueError
    if len_args > 1 and args[0] > args[1]:
        raise ValueError(f"'start' cannot be greater than 'end': myrange args are {args}")
    # TypeErrors
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError(f"myrange arguments must be type int: myrange args are {args}")

    # setup the start, stop, and step values for the "myrange" function

    if len_args == 1:     # myrange has one argument
        start = 0
        end = args[0]
        step = 1
    elif len_args == 2:   # myrange has two arguments
        start = args[0]
        end = args[1]
        step = 1
    elif len_args == 3:   # myrange has three arguments
        start = args[0]
        end = args[1]
        step = args[2]
    else:                 # myrange has arguments outside bounds of one, two, or three
        start = None
        end = None
        step = None

    n = start
    while n < end:
        yield n
        n += step


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



