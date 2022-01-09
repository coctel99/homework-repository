from homework2.task5 import make_custom_range


def test_custom_range_string():
    """Testing that custom range function makes range from string."""
    rng = make_custom_range("abcdefghijklmnopqrstuvwxyz", "g")
    assert rng == ['a', 'b', 'c', 'd', 'e', 'f']


def test_custom_range_string_2_param():
    """Testing that custom range function makes range from one arg
    to another from string."""
    rng = make_custom_range("abcdefghijklmnopqrstuvwxyz", "g", "p")
    assert rng == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


def test_custom_range_string_3_param():
    """Testing that custom range function makes range from one arg
    to another with specified step from string."""
    rng = make_custom_range("abcdefghijklmnopqrstuvwxyz", "g", "p", 2)
    assert rng == ['g', 'i', 'k', 'm', 'o']


def test_custom_range_int_list():
    """Testing that custom range function makes range from int list."""
    rng = make_custom_range([1, 2, 3, 4, 5, 6, 7], 4)
    assert rng == [1, 2, 3]


def test_custom_range_negative_int_list():
    """Testing that custom range function makes range from int list."""
    rng = make_custom_range([-1, -2, -3, -4, -5, -6, -7], -4)
    assert rng == [-1, -2, -3]


def test_custom_range_int_list_2_param():
    """Testing that custom range function makes range from one arg
    to another from int list."""
    rng = make_custom_range([1, 2, 3, 4, 5, 6, 7], 3, 6)
    assert rng == [3, 4, 5]


def test_custom_range_negative_int_list_2_param():
    """Testing that custom range function makes range from one arg
    to another from int list."""
    rng = make_custom_range([-1, -2, -3, -4, -5, -6, -7], -3, -6)
    assert rng == [-3, -4, -5]


def test_custom_range_int_list_3_param():
    """Testing that custom range function makes range from one arg
    to another with specified step from int list."""
    rng = make_custom_range([1, 2, 3, 4, 5, 6, 7], 3, 6, 2)
    assert rng == [3, 5]


def test_custom_range_negative_int_list_3_param():
    """Testing that custom range function makes range from one arg
    to another with specified step from int list."""
    rng = make_custom_range([-1, -2, -3, -4, -5, -6, -7], -3, -6, 2)
    assert rng == [-3, -5]


def test_custom_range_string_list():
    """Testing that custom range function makes range from string list."""
    rng = make_custom_range(["a", "b", "c", "d", "e",
                             "f", "g", "h", "i", "j"], "g")
    assert rng == ['a', 'b', 'c', 'd', 'e', 'f']


def test_custom_range_one_bound_and_step():
    """Testing that custom range function makes one-bound range with
    specified step."""
    rng = make_custom_range([1, 2, 3, 4, 5, 6, 7], bound=4, step=2)
    assert rng == [1, 3]


def test_custom_range_inverted():
    rng = make_custom_range([1, 2, 3, 4, 5, 6, 7], 6, 2)
    assert rng == [6, 5, 4, 3]


def test_custom_range_inverted_step():
    rng = make_custom_range([1, 2, 3, 4, 5, 6, 7], 6, 2, -2)
    assert rng == [6, 4]


def test_custom_range_negative_inverted_step():
    """Testing that custom range function makes range from one arg
    to another with specified step from int list."""
    rng = make_custom_range([-1, -2, -3, -4, -5, -6, -7], -6, -2, -2)
    assert rng == [-6, -4]
