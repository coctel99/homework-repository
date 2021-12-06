from homework7.task1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            "key4": (0, {1, (2, 3), "RED"}, [4]),
        },
    },
    "fourth": "RED",
    "RED": None,
}


def test_find_occurrences():
    """Testing that 7 occurrences are found in example_tree."""
    assert find_occurrences(example_tree, "RED") == 7


def test_empty_tree():
    """Testing that empty tree gives 0 occurrences."""
    assert find_occurrences({}, "RED") == 0


def test_no_occurrences():
    """Testing that 0 occurrences are found."""
    assert find_occurrences(example_tree, True) == 0
