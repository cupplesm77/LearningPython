# subprocess_driver.py

import subprocess

proc = subprocess.run([
    'python3',
    'findpattern.py',
    '--prefix FOUND',
    'like',
    'pattern.txt',
    ])

proc.check_returncode()