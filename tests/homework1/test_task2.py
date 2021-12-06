import pytest

from homework1.task2 import check_if_fibonacci_sequence


def test_positive_case():
    """Testing that actual Fibonacci sequence gives True."""
    assert check_if_fibonacci_sequence([0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
                                        55, 89, 144, 233, 377, 610, 987,
                                        1597, 2584, 4181, 6765])


@pytest.mark.parametrize("wrong_sequence", [
    [0, 0],
    [1, 1, 1],
    [0, 2],
    [1, 4],
    [0, 1, 1, 2, 3, 4]
])
def test_negative_case(wrong_sequence):
    """Testing that non-Fibonacci sequence gives False."""
    assert not check_if_fibonacci_sequence(wrong_sequence)


@pytest.mark.parametrize("Fibonacci_slice", [
    [0, 1],
    [0, 1, 1],
    [1, 1, 2],
    [1, 2],
    [3],
    [13, 21]
])
def test_fibonacci_slice(Fibonacci_slice):
    """Testing that slice of Fibonacci sequence gives True."""
    assert check_if_fibonacci_sequence(Fibonacci_slice)
