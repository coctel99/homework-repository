from homework2.task2 import major_and_minor_elem


def test_list_of_even_length():
    """Testing that list of even length gives a correct result"""
    assert major_and_minor_elem([0, 1, 1, 1, 1]) == (1, 0)


def test_list_of_odd_length():
    """Testing that list of odd length gives a correct result"""
    assert major_and_minor_elem([0, 1]) == (0, 1)


def test_list_with_negative():
    """Testing that list with negative numbers gives a correct result"""
    assert major_and_minor_elem([-2, -1, -1, -1, -1]) == (-1, -2)


def test_list_of_strings():
    """Testing that list with strings gives a correct result"""
    assert major_and_minor_elem(["a", "b", "b", "a", "a"]) == ("a", "b")
