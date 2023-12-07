# findpattern.py

import sys


# demonstrating how main guard operates
print(f"we are using {__name__}")
print("")
def grepfile(pattern, path):
    with open(path) as handle:
        for line in handle:
            if pattern in line:
                yield line.rstrip("\n")


# main guard
if __name__ == "__main__":
    pattern, path = sys.argv[1:], sys.argv[2]
    for line in grepfile(pattern, path):
        print(line)
