from homework9.task1 import merge_sorted_files

FILE1 = "./tests/homework9/file1.txt"
FILE2 = "./tests/homework9/file2.txt"
FILE_LIST = [FILE1, FILE2]


def test_merge_from_two_files():
    """Testing that integers from two files are merged."""
    assert list(merge_sorted_files(FILE_LIST)) == [1, 2, 3, 4, 5, 6]
