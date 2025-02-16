from homework1.sample_project.calculator.calc import check_if_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_if_power_of_2(65536)


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_if_power_of_2(12)


def test_zero_input_case():
    """Testing th give False"""
    assert not check_if_power_of_2(0)
