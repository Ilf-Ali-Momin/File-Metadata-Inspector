import os
import datetime
from src.decorators import deco

class FileInspector:
    def __init__(self, path):
        self._path = path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def __str__(self):
        return f"FileInspector({self.path})"

    def __add__(self, other):
        return CombinedFileInspector(self.path, other.path)

    @staticmethod
    def get_file_size(path):
        return os.path.getsize(path)

    @classmethod
    def from_file(cls, path):
        return cls(path)

    def read_lines(self):
        with open(self.path, 'r') as file:
            for line in file:
                yield line

    @deco("green")
    def get_metadata(self):
        size = os.path.getsize(self.path)
        ctime = datetime.datetime.fromtimestamp(os.path.getctime(self.path))
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(self.path))
        return f"Size: {size} bytes, Created: {ctime}, Modified: {mtime}"


class CombinedFileInspector(FileInspector):
    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2

    def __str__(self):
        return f"CombinedFileInspector({self.path1}, {self.path2})"

    def read_lines(self):
        yield from super(CombinedFileInspector, self).read_lines()
        with open(self.path2, 'r') as file:
            for line in file:
                yield line