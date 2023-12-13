# config.py

import os
import logging

mode = os.environ.get('MODE', 'production')
print('Running mode:', mode)
if mode == 'production':
    print('Running production mode')
elif mode == 'development':
    print('Running in development mode')
else:
    print('Running Away!')

LOGLEVEL = logging.WARNING
LOGMODE = "a"
LOGFILE = "mylog.txt"


def init_logging():
    logging.basicConfig(level=LOGLEVEL, filename=LOGFILE, filemode=LOGMODE)


# overrides
try:
    from localconfig import *
except ImportError:
    pass
