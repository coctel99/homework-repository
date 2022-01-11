"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from itertools import zip_longest


def get_next_backwards(text: str):
    backspaces_number = 0
    for char in reversed(text):
        if char == "#":
            backspaces_number += 1
            continue
        elif backspaces_number:
            backspaces_number -= 1
            continue
        else:
            yield char


def backspace_compare(first: str, second: str) -> bool:
    """
    Compare two strings where '#' means a backspace
    :param first: First string to check
    :param second: Second string to check
    :return: True if the first string is equal to the second,
    otherwise return False
    """
    for char_first, char_second in zip_longest(get_next_backwards(first),
                                               get_next_backwards(second)):
        if char_first != char_second:
            return False
    return True


if __name__ == "__main__":
    comp = backspace_compare("##acdc##", "#ad#c")
    print(comp)
