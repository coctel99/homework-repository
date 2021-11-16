"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase,'g') == /
['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == /
['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == /
['p', 'n', 'l', 'j', 'h']

"""
from typing import Iterable, List


def custom_range(iterable: Iterable[any], n: any) -> List[any]:
    ranged_list = list(iterable)[:list(iterable).index(n)]
    return ranged_list


if __name__ == '__main__':
    print(custom_range("abcdefghijklmnopqrstuvwxyz", "g"))
    print(custom_range([1, 2, 3, 4, 5, 6, 7], 4))
