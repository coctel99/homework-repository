from homework2.task2 import major_and_minor_elem


def test_list_of_even_length():
    """Testing that list of even length gives a correct result."""
    assert major_and_minor_elem([0, 1, 1, 1, 1]) == (1, 0)


def test_list_of_odd_length():
    """Testing that list of odd length gives a correct result."""
    assert major_and_minor_elem([0, 1]) == (0, 1)


def test_list_with_negative():
    """Testing that list with negative numbers gives a correct result."""
    assert major_and_minor_elem([-3, -2, -2, -1, -1, -1]) == (-1, -3)


def test_list_of_strings():
    """Testing that list with strings gives a correct result"""
    assert major_and_minor_elem(["a", "b", "b", "a", "a"]) == ("a", "b")


def test_list_of_mixed_chars():
    """Testing that list with mixed data type values give a correct result."""
    mixed = ["a", "a", "a", 0, 1, 1, "1", "1", -1, -1,
             "-1", "-1", None, None, "None", "None"]
    assert major_and_minor_elem(mixed) == ("a", 0)
