import pytest

from homework9.task2 import Suppressor, suppress_exception


def test_suppress_exception_with_class():
    """Testing that no exception occurred."""
    value = 0
    with Suppressor(IndexError):
        value += [][2]
    assert value == 0


def test_suppress_exception_with_function():
    """Testing that no exception occurred."""
    value = 0
    with suppress_exception(IndexError):
        value += [][2]
    assert value == 0


def test_suppress_only_specified_exception_with_class():
    """Testing that only specified exception is being suppressed."""
    value = 0
    with pytest.raises(ZeroDivisionError), Suppressor(IndexError):
        value += 1 / 0


def test_suppress_only_specified_exception_with_function():
    """Testing that only specified exception is being suppressed."""
    value = 0
    with pytest.raises(ZeroDivisionError), suppress_exception(IndexError):
        value += 1 / 0
