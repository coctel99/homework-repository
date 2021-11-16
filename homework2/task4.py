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


def some_func(a, b):
    return a * b


def cache(func: Callable) -> Callable:
    cached = {}

    def wrapper(*args):
        if args in cached:
            return cached[args]
        else:
            cached[args] = func(*args)
            return func(*args)

    return wrapper


cache_func = cache(some_func)
some = 100, 200
val_1 = cache_func(100, 200)
val_2 = cache_func(100, 200)
assert val_1 == val_2
