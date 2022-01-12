import json

TOP_N = 10


def get_top_n(companies_list: list, sort: str, top_n=TOP_N, serialize=False):
    """
    Get Top-N companies with highest current price
    :param companies_list: List of Company objects
    :param sort: Parameter to sort: "current_price", "lowest_pe",
    "highest_growth", "most_profitable"
    :param top_n: Number of companies from the top to take
    :param serialize: Write objects to file if True
    :return: Top-N companies with highest current price
    """
    params = {
        "current_price": (lambda x: (x.current_price is None,
                                     x.current_price), True),
        "lowest_pe": (lambda x: (x.pe is None, x.pe), False),
        "highest_growth": (lambda x: (x.year_change is None,
                                      x.year_change), True),
        "most_profitable": (lambda x: (x.val_highest is not None
                                       and x.val_lowest is not None,
                                       x.val_highest - x.val_lowest
                                       if x.val_highest is not None
                                       and x.val_lowest is not None
                                       else None), True),
    }
    if sort not in params:
        raise AttributeError(f"Unknown sort parameter: {sort}")
    key, reverse = params.get(sort)
    top = sorted(companies_list, key=key, reverse=reverse)
    top = top[:top_n]
    if serialize:
        _serialize_objects(top, f"Top_{top_n}_{sort}.json")
    return top


def _serialize_objects(cls_list: list, filename: str):
    """
    Write attributes of list of objects to a json file
    :param cls_list: List of objects
    :param filename: Name of the json file
    """
    data = [cls.__dict__ for cls in cls_list]
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)
