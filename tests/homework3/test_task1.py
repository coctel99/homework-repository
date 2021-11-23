from homework3.task1 import cache_number_of_times


@cache_number_of_times(times=2)
def multiply(number_1, number_2) -> int:
    return number_1 * number_2


def test_cache_multiply_results_2_times():
    """Testing that multiply function results are cached 2 times."""
    cached1 = multiply(1, 2)
    cached2 = multiply(1, 2)
    noncached = multiply(1, 2)
    assert cached1 is cached2 and noncached is None


@cache_number_of_times(times=0)
def test_cache_multiply_results_0_times():
    """Testing that multiply function results are not cached."""
    noncached1 = multiply(1, 2)
    noncached2 = multiply(1, 2)
    noncached3 = multiply(1, 2)
    assert noncached1 and noncached2 and noncached3 is None


@cache_number_of_times()
def test_cache_multiply_results_any_times():
    """Testing that multiply function results are cached without
    restrictions."""
    cached1 = multiply(1, 2)
    cached2 = multiply(1, 2)
    cached3 = multiply(1, 2)
    assert cached1 is cached2 is cached3
