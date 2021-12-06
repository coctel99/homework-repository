"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Get number of occurrences of element in dict recursively
    :param tree: Dictionary to check
    :param element: Element to find
    :return: Number of occurrences of element in dict
    """
    number_of_occurrences = 0
    if isinstance(tree, dict):
        for val in tree.values():
            if val == element:
                number_of_occurrences += 1
            else:
                number_of_occurrences += find_occurrences(val, element)
    elif isinstance(tree, (list, tuple, set)):
        for val in tuple(tree):
            number_of_occurrences += find_occurrences(val, element)
    else:
        if element == tree and type(element) == type(tree):
            number_of_occurrences += 1
    return number_of_occurrences
