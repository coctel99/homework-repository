import json
import os

from homework10.task1 import Company
from homework10.top import TOP_N, get_top_n

COMPANIES = [
    Company("Company1", "CMP1", 1900.0, 63.9, 20.0, 1800.0, 2000.0),
    Company("Company2", "CMP2", 1700.0, 35.53, 18.0, 1600.0, 1800.0),
    Company("Company3", "CMP3", 100, -99.9, -120.34, 90.345, 220.2345),
    Company("Company4", "CMP4", 999, None, 56.5, None, None)
]


def test_get_top_n_current_price():
    """Testing that top-10 companies with highest current price are printed to
    a .json file."""
    comp_sorted = sorted(COMPANIES, key=lambda x: x.current_price,
                         reverse=True)
    comp_data = [comp.__dict__ for comp in comp_sorted]
    get_top_n(COMPANIES, "current_price", serialize=True)
    json_file = f"Top_{TOP_N}_current_price.json"
    with open(json_file) as fi:
        data = json.load(fi)
        assert comp_data == data
    os.remove(json_file)


def test_get_top_n_lowest_pe():
    """Testing that top-10 companies with lowest P/E Ratio are printed to a
    .json file."""
    comp_sorted = sorted(COMPANIES, key=lambda x: (x.pe is None, x.pe))
    comp_data = [comp.__dict__ for comp in comp_sorted]
    get_top_n(COMPANIES, "lowest_pe", serialize=True)
    json_file = f"Top_{TOP_N}_lowest_pe.json"
    with open(json_file) as fi:
        data = json.load(fi)
        assert comp_data == data
    os.remove(json_file)


def test_get_top_n_highest_growth():
    """Testing that top-10 companies with highest yearly growth are printed
    to a .json file."""
    comp_sorted = sorted(COMPANIES, key=lambda x: (x.year_change is None,
                                                   x.year_change),
                         reverse=True)
    comp_data = [comp.__dict__ for comp in comp_sorted]
    get_top_n(COMPANIES, "highest_growth", serialize=True)
    json_file = f"Top_{TOP_N}_highest_growth.json"
    with open(json_file) as fi:
        data = json.load(fi)
        assert comp_data == data
    os.remove(json_file)


def test_get_top_n_most_profitable():
    """Testing that top-10 companies providing highest income if bought on
    minimum and sold on maximum for the last year are printed to a .json
    file."""
    comp_sorted = sorted(COMPANIES,
                         key=lambda x: (x.val_highest is not None
                                        and x.val_lowest is not None,
                                        x.val_highest - x.val_lowest
                                        if x.val_highest is not None
                                        and x.val_lowest is not None
                                        else None), reverse=True)
    comp_data = [comp.__dict__ for comp in comp_sorted]
    get_top_n(COMPANIES, "most_profitable", serialize=True)
    json_file = f"Top_{TOP_N}_most_profitable.json"
    with open(json_file) as fi:
        data = json.load(fi)
        assert comp_data == data
    os.remove(json_file)
