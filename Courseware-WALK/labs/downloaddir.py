'''

>>> dd = DownloadDir.create()
>>> len(os.listdir(dd.path))
0

>>> dd.current_file() is None
True

>>> pubdir = _testdir()
>>> dd.move_downloaded_file(pubdir)
Traceback (most recent call last):
...
AssertionError: No downloaded file to publish yet

>>> _touch(path_join(dd.path, 'foo'))
>>> dd.current_file().endswith('foo')
True
>>> len(os.listdir(dd.path))
1

>>> _touch(path_join(dd.path, 'foo.crdownload'))
>>> dd.current_file().endswith('foo.crdownload')
True
>>> len(os.listdir(dd.path))
2


>>> dd2 = DownloadDir.create()
>>> _touch(path_join(dd2.path, 'foo2'))
>>> _touch(path_join(dd2.path, 'foo2.txt'))
>>> dd2.current_file()
Traceback (most recent call last):
...
DownloadDir.InvalidStateException: ['foo2', 'foo2.txt']


>>> dd3 = DownloadDir.create()
>>> _touch(path_join(dd3.path, 'foo3'))
>>> _touch(path_join(dd3.path, 'foo3.crdownload'))
>>> _touch(path_join(dd3.path, 'foo3.extra'))
>>> dd3.current_file()
Traceback (most recent call last):
...
DownloadDir.InvalidStateException: ['foo3', 'foo3.crdownload', 'foo3.extra']


>>> dd4 = DownloadDir.create()
>>> _touch(path_join(dd4.path, 'foo4'))
>>> dd4.current_file().endswith('foo4')
True

>>> len(os.listdir(pubdir))
0
>>> len(os.listdir(dd4.path))
1

>>> dd4.move_downloaded_file(pubdir)

>>> len(os.listdir(pubdir))
1
>>> len(os.listdir(dd4.path))
0

>>> dd_path = dd.path
>>> file_exists(dd_path)
True
>>> del dd
>>> file_exists(dd_path)
False

'''

# These utility functions are used by the tests above. Don't touch 'em!

def _testdir():
    import shutil
    import tempfile
    import atexit
    dirname = tempfile.mkdtemp()
    atexit.register(lambda: shutil.rmtree(dirname))
    return dirname

def _touch(path):
    "Create an empty file at path, if it doesn't already exist."
    from pathlib import Path
    p = Path(path)
    p.touch()

from os.path import join as path_join
from os.path import exists as file_exists


# Write your code here:



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python. Copyright MigrateUp LLC. All rights reserved.

