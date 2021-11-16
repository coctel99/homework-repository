from homework2.task4 import cache


def some_func(a, b):
    return a*b


def test_cache_fucntion():
    """Testing that cache function returns value of initial function"""
    cached = cache(some_func)
    assert cached(100, 200) == some_func(100, 200)


def test_cached_values_in_fucntion():
    """Testing that cache function cashes output of the initial function"""
    cached = cache(some_func)
    val1 = cached(100, 200)
    val2 = cached(100, 200)
    assert val1 == val2
