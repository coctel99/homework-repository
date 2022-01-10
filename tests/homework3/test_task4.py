from homework3.task4 import is_armstrong


def test_positive_case():
    """Testing that actual Armstrong number gives True."""
    assert is_armstrong(153)


def test_negative_case():
    """Testing that non-Armstrong number gives False."""
    assert not is_armstrong(10)


def test_zero_case():
    """Testing that 0 gives True."""
    assert is_armstrong(0)


def test_one_case():
    """Testing that 1 gives True."""
    assert is_armstrong(1)
