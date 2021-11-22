from homework1.task5 import find_maximal_subarray_sum


def test_on_not_empty_list():
    """Test finding maximal subarray sum."""
    assert find_maximal_subarray_sum([0, 1, 2, 3, 2, 1, 0], 2) == 5


def test_on_empty_list():
    """Test finding maximal subarray sum in empty list."""
    assert find_maximal_subarray_sum([], 2) == 0


def test_on_not_empty_list_with_k_larger_than_list_length():
    """Test finding maximal subarray sum with subarray length larger
    than initial one."""
    assert find_maximal_subarray_sum([0, 1, 2, 3, 2, 1, 0], 100) == 9


def test_on_not_empty_list_with_zero_k():
    """Test finding maximal subarray sum with subarray length zero."""
    assert find_maximal_subarray_sum([0, 1, 2, 3, 2, 1, 0], 0) == 0
