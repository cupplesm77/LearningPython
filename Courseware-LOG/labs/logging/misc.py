# misc.py

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
# logging.basicConfig(filename='test.log', level=logging.DEBUG, filemode="a")


logging.debug("Howdy there, bug")
logging.warning("Watch Out!")
logging.error("Ouch!")

template = "I am going to %s"
logging.info(template, "Town!")




