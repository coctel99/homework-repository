"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator
from itertools import zip_longest
from contextlib import ExitStack


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """
    Merge integers from a number of files into one iterator
    :param file_list: List of files to merge
    :return: Iterator with integers from specified files
    """
    with ExitStack() as stack:
        files = [stack.enter_context(open(file_name)) for file_name in file_list]
        merged_string = []

        for lines in zip_longest(*files):
            merged_string.extend([*(map(int, lines))])
        return iter(merged_string)
