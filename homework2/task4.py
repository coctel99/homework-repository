"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    """

    Save results of all executions of given function

    :param func: A function, which results we need to cache
    :return: A wrapper function, which adds arguments and results
    of given function to he dict, and reads them from it
    """
    cached = {}

    @wraps(func)
    def wrapper(*args):
        """

        Add arguments and results of given function to the dict
        and read them from it

        :param args: Arguments of given function
        :return: Result of given function, or cached result,
        if it was already executed
        """
        if args in cached:
            return cached[args]
        else:
            cached[args] = func(*args)
            return func(*args)

    return wrapper
