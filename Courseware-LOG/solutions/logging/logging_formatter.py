'''
>>> LOGFILE_STANDARD
'logging_formatter-standard.txt'
>>> LOGFILE_CSV
'logging_formatter-csv.txt'
>>> LOGFILE_JSON
'logging_formatter-json.txt'

These lines reset the log files to empty for each test run.
>>> truncate_file(LOGFILE_STANDARD)
>>> truncate_file(LOGFILE_CSV)
>>> truncate_file(LOGFILE_JSON)

>>> my_logger.name
'root'
>>> my_logger.warning("There's a loose board right there.")
>>> my_logger.error("Auxiliary disk full")
>>> my_logger.info("Vancouver Island is 460 km in length.")

>>> print_file(LOGFILE_STANDARD)
WARNING:root:There's a loose board right there.
ERROR:root:Auxiliary disk full
INFO:root:Vancouver Island is 460 km in length.

>>> print_file(LOGFILE_CSV)
root,WARNING,There's a loose board right there.
root,ERROR,Auxiliary disk full
root,INFO,Vancouver Island is 460 km in length.

>>> print_file(LOGFILE_JSON)
{"logger":"root", "level":"WARNING", "message":"There's a loose board right there."}
{"logger":"root", "level":"ERROR", "message":"Auxiliary disk full"}
{"logger":"root", "level":"INFO", "message":"Vancouver Island is 460 km in length."}
'''

LOGFILE_STANDARD = 'logging_formatter-standard.txt'
LOGFILE_CSV = 'logging_formatter-csv.txt'
LOGFILE_JSON = 'logging_formatter-json.txt'

def truncate_file(path):
    # Make sure a file is empty.
    with open(path, 'w'): pass

def print_file(path):
    print(open(path).read(), end="")

# Write your code here:

import logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.INFO)

standard_handler = logging.FileHandler(LOGFILE_STANDARD)
standard_fmt = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
standard_handler.setFormatter(standard_fmt)
my_logger.addHandler(standard_handler)

csv_handler = logging.FileHandler(LOGFILE_CSV)
csv_fmt = logging.Formatter("%(name)s,%(levelname)s,%(message)s")
csv_handler.setFormatter(csv_fmt)
my_logger.addHandler(csv_handler)

json_handler = logging.FileHandler(LOGFILE_JSON)
json_fmt = logging.Formatter('{"logger":"%(name)s", "level":"%(levelname)s", "message":"%(message)s"}')
json_handler.setFormatter(json_fmt)
my_logger.addHandler(json_handler)

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2020 Aaron Maxwell. All rights reserved.
