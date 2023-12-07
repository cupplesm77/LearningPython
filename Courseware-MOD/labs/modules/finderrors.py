# finderrors.py

import sys
from findpattern import grepfile


# demonstrating how main guard operates
print(f"we are running {__name__}")
print("")
path = sys.argv[1]

for line in grepfile("ERROR",path):
    print(line)

