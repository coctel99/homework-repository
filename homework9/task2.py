"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with suppressor(IndexError):
...    [][2]
"""


class Suppressor:
    def __init__(self, exception: type(Exception)):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.exception is exc_type:
            return True


if __name__ == '__main__':
    with Suppressor(IndexError):
        [][2]
    print()
