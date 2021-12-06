def check_if_power_of_2(number: int) -> bool:
    """

    Check if integer is a power of 2

    :param number: Integer to check
    :return: Is number a power of 2 or not
    """
    if number == 0:
        return False
    return not (bool(number & (number - 1)))
