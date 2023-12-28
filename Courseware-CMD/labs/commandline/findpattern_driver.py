# subprocess_driver.py

"""
Used to run the findpattern.py
from an IDE
"""

import subprocess

proc = subprocess.run([
    'python',
    'findpattern.py',
    'like',
    '.\pattern.txt',
    '-i',
    '-p',
    'FOUND',
    '--limit',
    '7',
    ])

print(type(proc))
proc.check_returncode()