from homework4.task4 import fizzbuzz
import pytest


def test_get_fizzbuzz_numbers():
    """Testing that FizzBuzz number list is being created."""
    assert fizzbuzz(5) == ['1', '2', 'fizz', '4', 'buzz']


def test_get_zero_fizzbuzz_numbers():
    """Testing that FizzBuzz number list is empty."""
    assert fizzbuzz(0) == []


def test_get_type_error():
    """Testing that wrong data type raises TypeError."""
    with pytest.raises(TypeError):
        fizzbuzz("abc")


def test_get_value_error():
    """Testing that negative integer raises ValueError."""
    with pytest.raises(ValueError):
        fizzbuzz(-5)
