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


def custom_range(iterable: Iterable[any], iter_range: any, *args) -> List[any]:
    if not args:
        return list(iterable)[:list(iterable).index(iter_range)]
    if len(args) > 2:
        args = args[:3]
    if len(args) < 2:
        step = 1
    else:
        step = args[1]
    if args[0] > iter_range:
        return list(iterable)[list(iterable).index(iter_range):
                              list(iterable).index(args[0]):step]
    else:
        return list(iterable)[list(iterable).index(args[0]):
                              list(iterable).index(iter_range):step]


if __name__ == '__main__':
    print(custom_range("abcdefghijklmnopqrstuvwxyz", "g", "p", 2))
    print(custom_range([1, 2, 3, 4, 5, 6, 7], 3, 6, 2))
