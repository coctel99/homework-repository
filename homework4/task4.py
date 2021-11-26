"""
Write a function that takes a number N as an input and returns N FizzBuzz
numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть
картошку!"
"""
import doctest
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Get list of N FizzBuzz numbers

    FizzBuzz are numbers where any number divisible by three is
    replaced with the word "fizz", and any number divisible by five is
    replaced with the word "buzz"

    :param n: Length of FizzBuzz list
    :return: List of FizzBuzz numbers

    >>> fizzbuzz(10)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz']

    >>> fizzbuzz(0)
    []

    >>> fizzbuzz("abc")
    Traceback (most recent call last):
    ...
    TypeError: '<' not supported between instances of 'str' and 'int'

    >>> fizzbuzz(-5)
    Traceback (most recent call last):
    ...
    ValueError

    """
    if n < 0:
        raise ValueError

    fizzbuzz_list = []
    for val in range(1, n + 1):
        if val % 3 == 0:
            fizzbuzz_list.append("fizz")
        elif val % 5 == 0:
            fizzbuzz_list.append("buzz")
        else:
            fizzbuzz_list.append(str(val))
    return fizzbuzz_list


if __name__ == '__main__':
    doctest.testmod()
