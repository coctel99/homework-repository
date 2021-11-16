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
    with open(file_name) as fi:
        for n, line in enumerate(fi):
            if not line == "\n":
                line = line.replace("\n", "")
                if n == 0:
                    max_val = int(line)
                    min_val = int(line)
                else:
                    if int(line) > max_val:
                        max_val = int(line)
                    if int(line) < min_val:
                        min_val = int(line)

    fi.close()
    return max_val, min_val
