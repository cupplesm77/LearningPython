# textfiletools.py

import sys


# routine for finding lines having matching patterns in a text file
def matchinglines(pattern, path):
    with open(path) as handle:
        for line in handle:
            if pattern in line:
                yield line.rstrip('\n')


# routine for distinguishing individual words in a text file
def words_in_text(path):
    with open(path) as handle:
        for line in handle:  # note that the "handle" could be very long...potential bottleneck
            line = line.rstrip("\n")
            for word in line.split():
                yield word


def house_records(path):
    with open(path) as lines:
        record = {}
        for line in lines:
            if line == '\n':
                yield record
                record = {}
                continue
            key, value = line.rstrip('\n').split(': ', 1)
            record[key] = value
        yield record


# pattern, path = sys.argv[1], sys.argv[2]
# for line in matchinglines(pattern, path):
# print(line)

# path = "..\..\solutions\housedata.txt"

path = sys.argv[1]
print(path)
for line in house_records(path):
    print(line)
