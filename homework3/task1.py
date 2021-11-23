"""
In previous homework task 4, you wrote a cache function that remembers other
 function output value. Modify it to be a parametrized decorator, so that
 the following code:

    @cache(times=3)
    def some_function():
        pass

Would give out cached value up to times number only. Example:

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2,
                              use raw_input() instead

    >> f()
    ? 1
    '1'
    >> f()     # will remember previous value
    '1'
    >> f()     # but use it up to two times only
    '1'
    >> f()
    ? 2
    '2'
"""

from functools import wraps
from typing import Callable


def cache_number_of_times(times: int = None):
    """
    Process number of times cache can be received to cache function
    :param times: Number of times cache can be received
    :return: Cache function
    """

    def cache(func: Callable) -> Callable:
        """
        Save results of all executions of given function
        :param times: Number of times function could use cached values
        :param func: A function, which results we need to cache
        :return: A wrapper function, which adds arguments and results
        of given function to he dict, and reads them from it
        """
        cached = {}
        if times is not None:
            cached_times = times

        @wraps(func)
        def wrapper(*args):
            """
            Add arguments and results of given function to the dict
            and read them from it specified amount of times
            :param args: Arguments of given function
            :return: Result of given function, or cached result,
            if it was already executed
            """
            nonlocal cached_times
            if times is not None:
                cached_times -= 1
                if cached_times < 0:
                    cached[args] = None
            if args in cached:
                return cached[args]
            else:
                cached[args] = func(*args)
                return func(*args)

        return wrapper

    return cache
