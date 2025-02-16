from homework4.task5 import fizzbuzz


def test_get_fizzbuzz_numbers():
    """Testing that FizzBuzz number list is being created."""
    assert list(fizzbuzz(15)) == ['1', '2', 'fizz', '4', 'buzz',
                                  'fizz', '7', '8', 'fizz', 'buzz',
                                  '11', 'fizz', '13', '14', 'buzz']


def test_get_zero_fizzbuzz_numbers():
    """Testing that FizzBuzz number list is empty."""
    assert list(fizzbuzz(0)) == []
