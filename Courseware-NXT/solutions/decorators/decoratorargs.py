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

def mod(value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) % value
        return wrapper
    return decorator

def repeat(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # In Python, "_" is sometimes used as a dummy variable, e.g. when using range() to simply repeat.
            for _ in range(count):
                # By its nature, this decorator makes the most sense
                # to apply to functions that don't return any value at
                # all.  Here, I'm writing it so wrapper() returns
                # whatever value func() returns the last time it's
                # called. But the tests will pass even if wrapper()
                # returned nothing (i.e. returned None).
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

def transform(a, b):
    def decorator(func):
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return a * value + b
        return wrapper
    return decorator

def clip(lower, upper):
    # Defensive assertion. Doesn't make sense if lower > upper
    assert upper >= lower, (upper, lower)
    def decorator(func):
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if value > upper:
                value = upper
            elif value < lower:
                value = lower
            return value
        return wrapper
    return decorator

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python. Copyright MigrateUp LLC. All rights reserved.
