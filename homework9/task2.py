"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with suppressor(IndexError):
...    [][2]
"""
import contextlib


class Suppressor:
    def __init__(self, *exceptions: type(Exception)):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            return True


@contextlib.contextmanager
def suppress_exception(*exceptions: type(Exception)):
    try:
        yield
    except exceptions:
        pass
