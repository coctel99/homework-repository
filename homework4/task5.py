"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in
this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator

# Predeclared [0, 100] values. Took this approach from youtube video above
FIZZERS = [''] + ([''] * 2 + ['fizz']) * 33 + ['']
BUZZERS = [''] + ([''] * 4 + ['buzz']) * 20


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """
    Generate N FizzBuzz numbers
    :param n: Amount of FizzBuzz numbers
    """
    num = 1
    while num <= n:
        f = FIZZERS[num]
        b = BUZZERS[num]
        s = str(num)
        smth = b or f or s
        yield smth
        num += 1
