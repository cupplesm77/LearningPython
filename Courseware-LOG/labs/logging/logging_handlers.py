'''

>>> LOGFILE_TERSE
'logging_handlers-terse-log.txt'
>>> LOGFILE_VERBOSE
'logging_handlers-verbose-log.txt'
>>> LOGFILE_THOROUGH
'logging_handlers-thorough-log.txt'

These lines reset the log files to empty for each test run.
>>> truncate_file(LOGFILE_TERSE)
>>> truncate_file(LOGFILE_VERBOSE)
>>> truncate_file(LOGFILE_THOROUGH)

>>> my_logger.name
'root'
>>> my_logger.critical("Important news!")
>>> my_logger.error("Printer not found")
>>> my_logger.warning("Printer seems to be on fire")
>>> my_logger.info("It used to be a nice printer.")
>>> my_logger.debug("I bought it at a garage sale.")

This line prints out what's written to the log file so far.
>>> print(open(LOGFILE_TERSE).read(), end="")
Important news!
Printer not found

>>> print_file(LOGFILE_VERBOSE)
Important news!
Printer not found
Printer seems to be on fire
It used to be a nice printer.
I bought it at a garage sale.

>>> print_file(LOGFILE_THOROUGH)
Important news!
Printer not found
Printer seems to be on fire
It used to be a nice printer.

'''
LOGFILE_TERSE = 'logging_handlers-terse-log.txt'
LOGFILE_VERBOSE = 'logging_handlers-verbose-log.txt'
LOGFILE_THOROUGH = 'logging_handlers-thorough-log.txt'

def truncate_file(path):
    # Make sure a file is empty.
    with open(path, 'w'): pass

def print_file(path):
    print(open(path).read(), end="")

# Write your code here:



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2020 Aaron Maxwell. All rights reserved.
