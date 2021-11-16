"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such
that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    num_of_tuples = 0

    if a and b and c and d:
        for _, i_val in enumerate(a):
            for _, j_val in enumerate(b):
                for _, k_val in enumerate(c):
                    for _, l_val in enumerate(d):
                        if i_val + j_val + k_val + l_val == 0:
                            num_of_tuples += 1

    return num_of_tuples
