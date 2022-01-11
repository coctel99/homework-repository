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
    if tree is element:
        return 1

    if isinstance(tree, dict):
        list_of_values = [*tree.values()]
    elif isinstance(tree, (list, tuple, set)):
        list_of_values = list(tree)
    else:
        # If not iterable element and not a target element
        return 0

    number_of_occurrences = 0
    for val in list_of_values:
        if val is tree:
            # If value is a link to iterable itself, skip this value
            pass
        elif val is element:
            number_of_occurrences += 1
        else:
            number_of_occurrences += find_occurrences(val, element)

    return number_of_occurrences
