from homework2.task3 import combinations


def test_combinations_of_one_element_lists():
    assert combinations([1], [2]) == [[1, 2]]


def test_combinations_of_multi_element_lists():
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]
