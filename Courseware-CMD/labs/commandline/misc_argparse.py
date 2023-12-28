# misc_argparse.py

import argparse
from argparse import Namespace

# class Namespace:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#         print(f"Namespace dictionary created: {self.__dict__}")

pattern = 'like'
path = '.\\pattern.txt'
ignore_case = True
prefix = 'like'
limit = None
count = 5

nspace = Namespace(pattern=pattern,
                   path=path,
                   ignore_case=ignore_case,
                   prefix=prefix,
                   limit=limit,
                   count=count,
                   )

print(nspace.__dict__)

print(f"YEP, nspace: {nspace.__dict__}")
print("")

# this won't work:
# nspace.print()

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
    cls.print = lambda cls: print(f"args dictionary: {cls}")
    return cls
#

Namespace = printNamespace(Namespace)
print(type(Namespace))
print("")

nspace = Namespace(pattern=pattern,
                   path=path,
                   ignore_case=ignore_case,
                   prefix=prefix,
                   limit=limit,
                   count=count,
                   )
print("")
print(type(nspace))
print("")

nspace.print()

#
#
#
#
# #
# # # ******* parser 1
# # parser1 = argparse.ArgumentParser()
# # parser1.add_argument("filename")
# # parser1.add_argument("destination")
# # print(type(parser1))
# # args1 = parser1.parse_args(["foo", "bar"])
# #
# # print(args1.filename)
# # print(args1.destination)
# # #print(args1)
# # print("")
# # parser2 = argparse.ArgumentParser()
# # print(type(parser2))
# # parser2.add_argument("filename")
# # parser2.add_argument("--type",
# #                      choices=["text", "json"],
# #                      default="text"
# #                      )
# #
# # args2 = parser2.parse_args(["data.txt", "--type", "json"])
# # print(args2.filename)
# # # 'data.txt'
# # print(args2.type)
# # # 'json'
# #
# # args2 = parser2.parse_args(["data.txt"])
# # print(args2.filename)
# # # 'data.txt'
# # print(args2.type)
# # # 'text'
# #
# #
