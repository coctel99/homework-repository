from homework7.task2 import backspace_compare


def test_compare_normal_strings():
    """Testing that two equal strings give True."""
    assert backspace_compare("abc", "abc")


def test_compare_strings_equal_with_backspaces():
    """Testing that two equal after backspacing strings give True."""
    assert backspace_compare("ab#c", "ad#c")


def test_compare_strings_unequal_with_backspaces():
    """Testing that two not equal after backspacing strings give False."""
    assert not backspace_compare("abc", "ab#c")


def test_compare_strings_with_backspaces_at_the_beginning():
    """Testing that backspacing at the beginning of strings give result."""
    assert backspace_compare("##acdc##", "#ad#c")
