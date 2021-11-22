from homework1.task4 import check_sum_of_four


def test_on_normal_list():
    """Testing normal case."""
    assert check_sum_of_four([0, 1], [0, -1], [0, 2], [0, -3]) == 3


def test_on_zero_list():
    """Testing zero list case."""
    assert check_sum_of_four([0], [0], [0], [0]) == 1


def test_on_empty_list():
    """Testing empty list case."""
    assert check_sum_of_four([], [], [], []) == 0
