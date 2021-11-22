"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such
that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from itertools import product
from typing import List


def check_sum_of_four(*args: List[int]) -> int:
    """

    Get number of tuples with sum of zero from four lists having one element
    from each list

    :param args: Lists to check
    :return: Number of tuples where sum of elements is zero
    """
    list_a, list_b, list_c, list_d, *_ = args
    number_of_tuples = 0
    combinations = product(list_a, list_b, list_c, list_d)
    for elements in combinations:
        if sum(elements) == 0:
            number_of_tuples += 1
    return number_of_tuples
