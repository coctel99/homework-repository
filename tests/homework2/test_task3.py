from homework2.task3 import combinations


def test_combinations_of_one_element_lists():
    """Testing that lists of size 1 give a correct combination of elements"""
    assert combinations([1], [2]) == [[1, 2]]


def test_combinations_of_multi_element_lists():
    """Testing that lists with a number of elements give a correct
    combinations of elements"""
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]


def test_combinations_of_zero_element_lists():
    """Testing that empty lists give an empty list as combination
    of elements"""
    assert combinations([], [], []) == []


def test_combinations_of_one_list():
    """Testing that one list give all its single elements as combinations"""
    assert combinations([1, 2, 3]) == [[1], [2], [3]]
