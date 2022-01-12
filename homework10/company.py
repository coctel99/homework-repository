from dataclasses import dataclass


@dataclass
class Company:
    name: str = None
    code: str = None
    current_price: float = None
    pe: float = None
    year_change: float = None
    val_lowest: float = None
    val_highest: float = None
