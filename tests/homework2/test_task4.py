from homework2.task4 import cache


def multiply(number1, number2):
    return number1 * number2


def test_cache_function():
    """Testing that cache function returns value of initial function."""
    cached = cache(multiply)
    assert cached(100, 200) == multiply(100, 200)


def test_cached_values_in_function():
    """Testing that cache function cashes output of the initial function."""
    cached = cache(multiply)
    val1 = cached(100, 200)
    val2 = cached(100, 200)
    assert val1 == val2
