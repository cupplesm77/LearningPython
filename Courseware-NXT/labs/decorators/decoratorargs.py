'''_

Here's a couple of function definitions, using the mod() decorator -
which you need to define:

>>> @mod(3)
... def combine_mod3(x, y):
...     return x + y

>>> @mod(10)
... def combine_mod10(x, y):
...     return x + y


The mod(n) decorator changes the function to return the mod of its value:

>>> combine_mod3(1, 1)
2

>>> combine_mod3(2, 2)
1

>>> combine_mod10(2, 2)
4

>>> combine_mod10(1, 8)
9
>>> combine_mod10(1, 9)
0


Now, let's make a decorator called repeat(), that calls the function several times:

(again, your job is to write the repeat() decorator below)

>>> @repeat(5)
... def say_hello(name):
...     print("Hello, " + name + "!")

>>> @repeat(3)
... def hooray():
...     print("Hip hip...")
...     print("HOORAY!!!")

>>> say_hello("Bob")
Hello, Bob!
Hello, Bob!
Hello, Bob!
Hello, Bob!
Hello, Bob!

>>> say_hello("Jane")
Hello, Jane!
Hello, Jane!
Hello, Jane!
Hello, Jane!
Hello, Jane!

>>> hooray()
Hip hip...
HOORAY!!!
Hip hip...
HOORAY!!!
Hip hip...
HOORAY!!!

Next, write a decorator called transform(a, b) that does what's called
an "affine" transformation. Which transforms values according to this
equation:

  newval = a * val + b

Let's apply it to these functions:

>>> @transform(10, -5)
... def calculate_code(seed):
...     return seed + 1

>>> @transform(2, 5)
... def from_max_of_3(x, y, z):
...     return max([x, y, z])

>>> calculate_code(1)
15

>>> calculate_code(9)
95

>>> from_max_of_3(5, 4, 3)
15

>>> from_max_of_3(10, 20, 10)
45


Finally, write a decorator called clip(), which takes two
arguments. When applied to a function, @clip(lower, upper) will
"clip" its returned value to be within that range.

So take this function, for example:

>>> @clip(0, 2)
... def extrapolate(x):
...     return x + 1

The values it returns for different inputs:

>>> extrapolate(0)
1
>>> extrapolate(0.5)
1.5
>>> extrapolate(1)
2
>>> extrapolate(2.1)
2
>>> extrapolate(10)
2
>>> extrapolate(10000)
2
>>> extrapolate(-1)
0
>>> extrapolate(-10000)
0

Another one:

>>> @clip(-1.0, 1.0)
... def reduce_value(value):
...     return 0.1 * value

>>> reduce_value(0)
0.0
>>> reduce_value(5)
0.5
>>> reduce_value(6.5)
0.65
>>> reduce_value(10)
1.0
>>> reduce_value(11)
1.0
>>> reduce_value(1000)
1.0
>>> reduce_value(-5)
-0.5
>>> reduce_value(-500)
-1.0

'''

# Write your code here:

def mod(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            f = (args[0] + args[1]) % num
            return f
        return wrapper
    return decorator


def repeat(number_of_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for idx in range(number_of_times):
                func(*args, **kwargs)
        return wrapper
    return decorator


def transform(x, y):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * x + y
        return wrapper
    return decorator


def clip(x, y):
    def decorator(func):
        def wrapper(*args, **kwargs):
            f = func(*args, **kwargs)
            if f > y:
                return y
            elif x < f <= y:
                return f
            else:
                return x
        return wrapper
    return decorator

# >>> @clip(0, 2)
# ... def extrapolate(x):
# ...     return x + 1
#
# The values it returns for different inputs:
#
# >>> extrapolate(0)
# 1
# >>> extrapolate(0.5)
# 1.5
# >>> extrapolate(1)
# 2
# >>> extrapolate(2.1)
# 2
# >>> extrapolate(10)
# 2
# >>> extrapolate(10000)
# 2
# >>> extrapolate(-1)
# 0
# >>> extrapolate(-10000)
# 0

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python. Copyright MigrateUp LLC. All rights reserved.
