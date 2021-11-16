from homework2.task5 import custom_range


def test_custom_range_string():
    """Testing that custom range function works on string"""
    assert custom_range("abcdefghijklmnopqrstuvwxyz",
                        "g") == ['a', 'b', 'c', 'd', 'e', 'f']


def test_custom_range_int_list():
    """Testing that custom range function works on int list"""
    assert custom_range([1, 2, 3, 4, 5], 3) == [1, 2]


def test_custom_range_string_list():
    """Testing that custom range function works on string list"""
    assert custom_range(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
                        "g") == ['a', 'b', 'c', 'd', 'e', 'f']
