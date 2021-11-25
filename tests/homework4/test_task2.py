import unittest.mock as mock

from homework4.task2 import count_dots_on_i

TEXT_STRING = "Some ii mocked text i"


def fake_urlopen(url: str, timeout: int = None):
    class FakeUrl:
        @staticmethod
        def read():
            return TEXT_STRING

        @staticmethod
        def readlines():
            return TEXT_STRING.split()
    return FakeUrl


def test_count_i():
    with mock.patch('urllib.request.urlopen', new=fake_urlopen):
        assert count_dots_on_i("some_url") == TEXT_STRING.count("i")
