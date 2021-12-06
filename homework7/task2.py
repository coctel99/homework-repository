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


def backspace_compare(first: str, second: str) -> bool:
    """
    Compare two strings where '#' means a backspace
    :param first: First string to check
    :param second: Second string to check
    :return: True if the first string is equal to the second,
    otherwise return False
    """
    buffer_first = []
    buffer_second = []
    for char in first:
        if buffer_first and char == "#":
            buffer_first.pop(-1)
        if char != "#":
            buffer_first.append(char)

    for char in second:
        if buffer_second and char == "#":
            buffer_second.pop(-1)
        if char != "#":
            buffer_second.append(char)
    return buffer_first == buffer_second
