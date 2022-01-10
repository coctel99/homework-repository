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


def make_custom_range(iterable: Iterable[any], bound: any,
                      second_bound: any = None,
                      step: int = None) -> List[any]:
    """
    Get arranged list from any iterable. Works backwards too

    Specified bound: Get a list from 0 element of given iterable to the given
    bound value

    Specified bound and second_bound: Get a list from given iterable from
    bound to the second_bound value

    Specified bound, second_bound and step: Get a list from given iterable
    from bound to the second_bound value with period of step value

    :param iterable: Any iterable of values
    :param bound: End of the range value if no other args, otherwise the
    beginning of the range
    :param second_bound: If specified, end of the range
    :param step: If specified, iteration period
    :return: A range from given iterable
    """
    iterable = list(iterable)
    if not bound or not bound and not second_bound:
        raise ValueError("Range bounds are not specified.")

    # Two-bound range
    bound_index = iterable.index(bound)
    if not second_bound:
        second_bound_index = bound_index
        bound_index = 0
    else:
        second_bound_index = iterable.index(second_bound)

    # Check if normal or inverted range
    if second_bound and bound_index > second_bound_index:
        if step is None:
            step = -1
        if step > 0:
            raise ValueError("For inverted range step should be negative.")
    else:
        if step is None:
            step = 1
        if step < 0:
            raise ValueError("Negative step value for not inverted range.")

    return iterable[bound_index:second_bound_index:step]
