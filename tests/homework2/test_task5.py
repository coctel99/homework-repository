from homework2.task5 import make_custom_range


def test_custom_range_string():
    """Testing that custom range function makes range from string."""
    assert make_custom_range("abcdefghijklmnopqrstuvwxyz",
                             "g") == ['a', 'b', 'c', 'd', 'e', 'f']


def test_custom_range_string_2_param():
    """Testing that custom range function makes range from one arg
    to another from string."""
    assert make_custom_range("abcdefghijklmnopqrstuvwxyz",
                             "g", "p") == ['g', 'h', 'i', 'j', 'k',
                                           'l', 'm', 'n', 'o']


def test_custom_range_string_3_param():
    """Testing that custom range function makes range from one arg
    to another with specified step from string."""
    assert make_custom_range("abcdefghijklmnopqrstuvwxyz",
                             "g", "p", 2) == ['g', 'i', 'k', 'm', 'o']


def test_custom_range_int_list():
    """Testing that custom range function makes range from int list."""
    assert make_custom_range([1, 2, 3, 4, 5, 6, 7], 4) == [1, 2, 3]


def test_custom_range_int_list_2_param():
    """Testing that custom range function makes range from one arg
    to another from int list."""
    assert make_custom_range([1, 2, 3, 4, 5, 6, 7], 3, 6) == [3, 4, 5]


def test_custom_range_int_list_3_param():
    """Testing that custom range function makes range from one arg
    to another with specified step from int list."""
    assert make_custom_range([1, 2, 3, 4, 5, 6, 7], 3, 6, 2) == [3, 5]


def test_custom_range_string_list():
    """Testing that custom range function makes range from string list."""
    assert make_custom_range(["a", "b", "c", "d", "e",
                              "f", "g", "h", "i", "j"],
                             "g") == ['a', 'b', 'c', 'd', 'e', 'f']
