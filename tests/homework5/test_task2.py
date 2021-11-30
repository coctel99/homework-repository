from functools import reduce

from homework5.task2 import print_result


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add__."""
    return reduce(lambda x, y: x + y, args)


def test_func_with_print(capsys):
    """Testing that function triggers print result."""
    custom_sum(1, 2, 3, 4)
    captured = capsys.readouterr()
    assert captured.out.strip() == "10"


def test_func_without_print(capsys):
    """Testing that original function is used."""
    without_print = custom_sum.__original_func
    without_print(1, 2, 3, 4)
    captured = capsys.readouterr()
    assert captured.out.strip() == ""
