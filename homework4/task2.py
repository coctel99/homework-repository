"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
>> count_dots_on_i("https://example.com/")
59
* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import urllib
from urllib.request import URLError


def count_dots_on_i(url: str) -> int:
    """
    Get number of 'i' letters in the HTML by the specified URL
    :param url: URL to check
    :return: Number of 'i' letters
    """
    try:
        number_of_i = 0
        contents = urllib.request.urlopen(url, timeout=10).readlines()
        for line in contents:
            line = str(line).strip()
            number_of_i += line.count("i")
        return number_of_i
    except URLError:
        raise ValueError(f"Unreachable {url}")
