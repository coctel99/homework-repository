"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from functools import lru_cache
from math import log, sqrt
from typing import Sequence


@lru_cache
def check_if_fibonacci_number(number: int) -> bool:
    """

    Check if integer is fibonacci number

    Based on formulas of the Fibonacci number identification in the wiki,
    x is a Fibonacci number if at list one of 5x^2 + 4 or 5x^2 - 4 is a
    perfect square

    :param number: A number to check
    :return: Is a fibonacci number or not
    """
    if sqrt(5 * number ** 2 + 4).is_integer() or \
            sqrt(5 * number ** 2 - 4).is_integer():
        return True
    return False


def get_position_in_fibonacci_sequence(number: int) -> int:
    """

    Get the position of the Fibonacci number in the Fibonacci sequence

    :param number: A Fibonacci number
    :return: A position of the number in the Fibonacci sequence
    """
    if number != 0:
        pos = round(
            log((number * sqrt(5) + sqrt(5 * number ** 2 + 4)) / 2,
                (1 + 5 ** 0.5) / 2)
        )
        return pos
    return 1


def check_if_fibonacci_sequence(data: Sequence[int]) -> bool:
    """

    Check if sequence is a Fibonacci sequence

    :param data: Sequence to check
    :return: Is sequence is a Fibonacci sequence or not
    """
    data = list(data)
    if len(data) == 1:
        if not check_if_fibonacci_number:
            return False
    elif len(data) == 2:
        if data == [1, 1]:
            return True
        if not (check_if_fibonacci_number(data[0]) and
                check_if_fibonacci_number(data[1])):
            return False
        elif get_position_in_fibonacci_sequence(data[1]) \
                - get_position_in_fibonacci_sequence(data[0]) != 1:
            return False
    elif len(data) > 2:
        if data == [0, 1, 1]:
            return True
        for current in range(len(data) - 2):
            if not data[current + 2] == data[current + 1] + data[current]:
                return False
    return True
