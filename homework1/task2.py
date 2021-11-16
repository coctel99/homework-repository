"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    for i in range(len(data) - 3):
        if not data[i + 2] == data[i + 1] + data[i]:
            return False
    return True
