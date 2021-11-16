from homework1.task2 import check_fibonacci


def test_positive_case():
    """Testing that actual Fibonacci sequence gives True"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
                            233, 377, 610, 987, 1597, 2584, 4181, 6765])


def test_negative_case():
    """Testing that non-Fibonacci sequence gives False"""
    assert not check_fibonacci([0, 1, 1, 2, 3, 5, 6, 7, 8])


def test_less_than_three_elements_in_the_list_case():
    """Testing that list of less than 3 elements gives False"""
    assert not check_fibonacci([0, 1])


def test_empty_list_case():
    """Testing that empty list gives False"""
    assert not check_fibonacci([])
