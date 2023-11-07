# decorators1.py

def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@shout
def say_hello(who):
    return f"Hello, {who}!"

print(say_hello("George"))

# Masking
def check_id(func):
    def wrapper(*args, **kwargs):
        print("ID of func: " + str(id(func)))
        return func(*args, **kwargs)
    print("ID of wrapper: " + str(id(wrapper)))
    return wrapper


@check_id
def f(x):
    return x * 3

f(2)


def printlog(func):
    def wrapper(*arg, **kwargs):
        print("CALLING: " + func.__name__)
        return func(*arg, **kwargs)
    return wrapper


@printlog
def f(n):
    return n + 2


print(f(3))


@printlog
def g(item1, item2):
    while True:
        for x in item1:
            for y in item2:
                yield x * y
        break


print(type(g))
x = g([1, 2, 3], [1, 2, 3])
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
