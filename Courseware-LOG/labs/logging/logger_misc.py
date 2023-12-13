# logger_misc.py

import logging
import sys


logger = logging.getLogger(__name__)
# set the default logger level
logger.setLevel(logging.DEBUG)

# set the file handler for an output file; note that we do not perform a setlevel on this file...defaults to the logger
log_file_handler = logging.FileHandler("logger.txt")

# set a file handler for the stdout;  note that we DO perform a more restrictive setlevel on the stdout
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.WARNING)

# implement formatted output from the logger
fmt = logging.Formatter("[%(levelname)s] - %(message)s")
stdout_handler.setFormatter(fmt)
log_file_handler.setFormatter(fmt)

# add the handlers to the logger
logger.addHandler(log_file_handler)
logger.addHandler((stdout_handler))

# check if the logger has one or more handlers
print(logger.hasHandlers())

# start logging...note that we are not using format at this stage
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is an warning message")
logger.error("This is an error message")
logger.critical("This is an critical message")





