from homework2.task2 import major_and_minor_elem


def test_list_of_even_length():
    assert major_and_minor_elem([0, 1, 1, 1, 1]) == (1, 0)


def test_list_of_odd_length():
    assert major_and_minor_elem([0, 1]) == (0, 1)
