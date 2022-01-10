from homework3.task1 import cache_number_of_times


def test_cache_multiply_results_2_times():
    """Testing that multiply function results are cached 2 times."""
    @cache_number_of_times(2)
    def multiply(number_1: float, number_2: float) -> float:
        return float(number_1 * number_2)

    cached1 = multiply(1, 2)
    cached2 = multiply(1, 2)
    noncached = multiply(1, 2)
    assert cached1 is cached2 and cached2 is not noncached


def test_cache_multiply_results_0_times():
    """Testing that multiply function results are not cached."""
    @cache_number_of_times(0)
    def multiply(number_1: float, number_2: float) -> float:
        return float(number_1 * number_2)

    noncached1 = multiply(1, 2)
    noncached2 = multiply(1, 2)
    noncached3 = multiply(1, 2)
    assert noncached1 is not noncached2 and noncached2 is not noncached3


def test_cache_multiply_results_any_times():
    """Testing that multiply function results are cached without
    restrictions."""
    @cache_number_of_times()
    def multiply(number_1: float, number_2: float) -> float:
        return float(number_1 * number_2)

    cached1 = multiply(1, 2)
    cached2 = multiply(1, 2)
    cached3 = multiply(1, 2)
    assert cached1 is cached2 is cached3
