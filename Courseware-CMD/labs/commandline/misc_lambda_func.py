# misc_lambda_func.py

from argparse import Namespace

# FYI: This is the argparse Namespce:
# class Namespace(_AttributeHolder):
#     def __init__(self, **kwargs: Any) -> None: ...
#     def __getattr__(self, name: str) -> Any: ...
#     def __setattr__(self, __name: str, __value: Any) -> None: ...
#     def __contains__(self, key: str) -> bool: ...
#     def __eq__(self, other: object) -> bool: ...

def printNamespace(cls):
    """
    add enhanced printing to the cls
    Parameters
    ----------
    cls  class passed to printNamespace

    Returns
    -------
    cls   modified to print the namespace (added a print attribute)
    """

    # using a traditional functional approach to setting up the new printing attribute:
    # def f(x):
    #     print(f"args dictionary: {x}")
    #
    # cls.printArgs = f

    # using a lambda function rather than a traditional function:
    cls.printArgs = lambda x: print(f"args dictionary: {x}")

    return cls


Namespace = printNamespace(Namespace)

nspace = Namespace(x = 22, y=44, z='Howdy')

print(nspace)

nspace.printArgs()

def func(value):
    return value + 1

f = func
print(f(7))


y = lambda x: x +1
print(y(7))

z = lambda self, x, y: x + y
print(z(0, 8, 8))