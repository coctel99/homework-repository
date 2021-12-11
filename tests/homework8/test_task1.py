from homework8.task1 import make_key_value_storage

FILE_PATH = "./tests/homework8/test.txt"
FILE_PATH2 = "./tests/homework8/test.txt"


@make_key_value_storage
class SomeClass:
    pass


@make_key_value_storage
class SomeClassWithInit:
    def __init__(self, name):
        self.name = name


def test_get_value_with_dot_operator():
    """Testing that '.' operator return value of the key from file."""
    a = SomeClass(FILE_PATH)
    assert a.name == "Ivan"


def test_get_value_with_square_brackets_operator():
    """Testing that '[]' operator return value of the key from file."""
    a = SomeClass(FILE_PATH)
    assert a["name"] == "Ivan"


def test_original_init_is_not_overwritten():
    """Testing that original function __init__ is not being overwritten."""
    a = SomeClassWithInit(name="Sasha", path_to_file=FILE_PATH)
    assert a["name"] == "Sasha"


def test_two_instances():
    """Testing that different class instances have different key-value
    storages."""
    a = SomeClass(FILE_PATH)
    b = SomeClass(FILE_PATH2)
    assert a["name"] == "Ivan" and b["name"] == "Alex"
