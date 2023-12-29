# findpattern.py
"""
Very simple program demonstrating the argparse package
Parse arguments from the command line and then reading a file based on the arguments

This routine can be run from the command line or from and IDE:  see the run_flag comments in the code.

use findpattern.py -h or --help for more information on this routine

For information on how to use the argparse package, see:
https://docs.python.org/3/library/argparse.html
"""

import argparse
from argparse import Namespace


def positive_int(value):
    """
    return a positive integer or raise a TypeError (from int(value) or ValueError (from raise)
    """
    number = int(value)
    if number <= 0:
        raise ValueError("Bad value: {}".format(str(value)))
    return number


# ************ adding a print attribute to the argparse Namespace class (monkey patch)
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


# ***************************************************************

def grepfile(pattern, path, ignore_case):
    with open(path) as handle:
        for line in handle:
            if ignore_case:
                if pattern in line.lower():
                    # print('yield line')
                    yield line.rstrip("\n")
            else:
                if pattern in line:
                    yield line.rstrip("\n")


def get_args():
    description = "Finds patterns in a file located at 'path' using 'pattern'."
    epilog = "Similar to grep, but with substring matching only."
    parser = argparse.ArgumentParser(description=description, epilog=epilog)
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("pattern", help="Substring pattern to match.")
    parser.add_argument('path', help="Path to file in which to search.")
    parser.add_argument('-i', '--ignore_case', action='store_true', help="Ignore case.")
    parser.add_argument('-p', '--prefix', default=" ", help="Prepend prefix to output lines.")
    group.add_argument('--limit', default=None, type=positive_int,
                       help="Show only this many matches. Default is show all.")
    group.add_argument('-c', '--count', default=None, type=positive_int,
                       help="Count only this many matches at most. Default is to count all.")
    return parser.parse_args()


# helper functions
def setup_index_counting(args):
    if args.limit is not None:
        index_count = args.limit
    elif args.count is not None:
        index_count = args.count
    else:
        raise ValueError("Limit and count cannot be both be specified at the same time.")
    return index_count


def output(args, line):
    # arguments limit and count are mutually exclusive
    if args.limit is not None:
        print(f'"{args.prefix}" Found: {line}')
    elif args.count is not None:
        print(f"Found: {index} {args.prefix}'s")


if __name__ == "__main__":
    # run_flag = False if running script from command line; True otherwise
    run_flag = False
    args = get_args()
    args.printArgs()
    index = 0
    index_count = setup_index_counting(args)
    # arguments limit and count are mutually exclusive
    if args.limit is not None or args.count is not None:
        for line in grepfile(args.pattern, args.path, args.ignore_case):
            index += 1
            # output the information based on
            output(args, line)
            if index >= index_count:
                print("reached the specified limit/count of number of 'pattern' lines read from pattern file...break!")
                break
    else:
        for line in grepfile(args.pattern, args.path, args.ignore_case):
            print(f"{args.prefix}: {line}")

    print(f"That's all folks!")
