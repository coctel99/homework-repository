from homework1.task3 import find_maximum_and_minimum


def test_on_file_with_line_delimetered_integers():
    """Testing that function finds maximum and minimum if the file."""
    assert find_maximum_and_minimum(
        "./tests/homework1/some_file.txt") == (19, 0)
