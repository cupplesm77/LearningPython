# misc_argparse.py

import argparse


# ******* parser 1
parser1 = argparse.ArgumentParser()
parser1.add_argument("filename")
parser1.add_argument("destination")
print(type(parser1))
args1 = parser1.parse_args(["foo", "bar"])

print(args1.filename)
print(args1.destination)
#print(args1)
print("")
parser2 = argparse.ArgumentParser()
print(type(parser2))
parser2.add_argument("filename")
parser2.add_argument("--type",
                     choices=["text", "json"],
                     default="text"
                     )

args2 = parser2.parse_args(["data.txt", "--type", "json"])
print(args2.filename)
# 'data.txt'
print(args2.type)
# 'json'

args2 = parser2.parse_args(["data.txt"])
print(args2.filename)
# 'data.txt'
print(args2.type)
# 'text'


