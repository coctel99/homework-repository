"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with suppressor(IndexError):
...    [][2]
"""
import contextlib


class Suppressor:
    def __init__(self, exception: type(Exception)):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.exception is exc_type:
            return True


@contextlib.contextmanager
def suppress_exception(exception: type(Exception)):
    try:
        yield
    except exception:
        pass
