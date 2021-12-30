"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


# Metaclass
class SimplifiedEnum(type):
    def __new__(mcs, name, bases, clsdict):
        cls_instance = super().__new__(mcs, name, bases, clsdict)
        cls_keys = f"_{name}__keys"
        if getattr(cls_instance, cls_keys, None):
            for key in getattr(cls_instance, cls_keys):
                setattr(cls_instance, key, key)
        return cls_instance
