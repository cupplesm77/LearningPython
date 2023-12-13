# misc_test_override.py

# sets the logging configuration
import logging
import config

# initialize logging ---- note that logging override is found in the config module
config.init_logging()

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")




