# decorators1.py


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
