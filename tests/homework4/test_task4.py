from homework4.task4 import fizzbuzz


def test_get_fizzbuzz_numbers():
    """Testing that FizzBuzz number list is being created."""
    assert fizzbuzz(5) == ['1', '2', 'fizz', '4', 'buzz']
