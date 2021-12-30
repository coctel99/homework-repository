from enum import Enum

from homework11.task1 import SimplifiedEnum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class ColorsEnumSimple(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class ColorsEnumMixed(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE")
    ORANGE = "ORANGE"
    BLACK = "BLACK"


def test_get_simple_enum_value():
    """Testing that we can get value with class attribute."""
    assert ColorsEnum.RED.value == ColorsEnumSimple.RED == "RED"


def test_get_mixed_enum_value_from_keys():
    """Testing that we can get value from __keys with class attribute."""
    assert ColorsEnumMixed.RED == "RED"


def test_get_mixed_enum_value_from_class_attrs():
    """Testing that original attributes are saved."""
    assert ColorsEnumMixed.BLACK == "BLACK"
