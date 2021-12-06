"""
Write down the function, which reads input line-by-line, and find maximum
and minimum values. Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return (1, 5)
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """

    Get the maximal and minimal values from file

    :param file_name: Name or route of the file to check
    :return: Tuple of 2 values: maximal and minimal
    """

    with open(file_name) as fi:
        for line_number, line in enumerate(fi):
            if line != "\n":
                line = int(line.strip())
                if line_number == 0:
                    max_val, min_val = line, line
                else:
                    if line > max_val:
                        max_val = line
                    if line < min_val:
                        min_val = line

    return max_val, min_val
