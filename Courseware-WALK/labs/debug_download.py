# debug_download.py

import os
import shutil
import tempfile
from os.path import exists as file_exists


class DownloadDir:
    class InvalidStateException(Exception):
        """Indicates contents of download directory are invalid/corrupted"""

    def __init__(self, path):
        self.path = path

    @classmethod
    def create(cls):
        download_dir = tempfile.mkdtemp()
        cls._check_path(download_dir)
        return cls(download_dir)

    def __del__(self):
        self._check_path(self.path)
        shutil.rmtree(self.path)

    @staticmethod
    def _check_path(path):
        assert len(path) > 2, path


dd = DownloadDir.create()
print(len(os.listdir(dd.path)))
# 0

dd_path = dd.path
print(file_exists(dd_path))

del dd
print(file_exists(dd_path))
