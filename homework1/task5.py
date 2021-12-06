"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """

    Get maximal sum of elements of subarray with length less or equal to k

    :param nums: List of integers to check
    :param k: Subarray length
    :return: Maximal sum of elements
    """
    if k > len(nums):
        k = len(nums)
    k_sum = 0
    for i in range(len(nums) - k + 1):
        if sum(nums[i: i + k]) > k_sum:
            k_sum = sum(nums[i: i + k])

    return k_sum
