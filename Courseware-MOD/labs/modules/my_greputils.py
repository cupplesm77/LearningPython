# greputils.py

def grepfile(pattern, path):
    with open(path) as handle:
        for line in handle:
            if pattern in line:
                yield line.rstrip("\n")


def grepfilei(pattern, path):
    """
    case insensitive search
    """
    pattern = pattern.lower()
    with open(path) as handle:
        for line in handle:
            if pattern in line.lower():
                yield line.rstrip("\n")