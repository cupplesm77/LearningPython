# findpattern.py

import sys

def matchinglines(pattern, path):
    with open(path) as handle:
        for line in handle:
            if pattern in line:
                yield line.rstrip('\n')


pattern, path = sys.argv[1], sys.argv[2]
for line in matchinglines((pattern, path):
    print(line)

