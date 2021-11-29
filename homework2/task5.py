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


def make_custom_range(iterable: Iterable[any], iter_range: any, *args) -> List[any]:
    """

    Get arranged list from any iterable. Works backwards too

    No args: Get a list from 0 element of given iterable to the given
    iter_range value

    1 args: Get a list from given iterable from iter_range to the args value

    2 args: Get a list from given iterable from iter_range to the args 1st
    value with step of args 2nd value

    :param iterable: Any iterable of values
    :param iter_range: End of the range value if no args, otherwise the
    beginning of the range
    :param args: Optional. 1st - end of the range value, 2nd - step size
    :return: A range from given iterable
    """
    iterable = list(iterable)
    if not args:
        end_index = iterable.index(iter_range)
        return iterable[:end_index]
    if len(args) > 2:
        args = args[:3]
    if len(args) < 2:
        step = 1
    else:
        step = args[1]
    if args[0] > iter_range:
        start_index = iterable.index(iter_range)
        end_index = iterable.index((args[0]))
        return iterable[start_index:end_index:step]
    else:
        start_index = iterable.index((args[0]))
        end_index = iterable.index(iter_range)
        return iterable[start_index:end_index:step]
