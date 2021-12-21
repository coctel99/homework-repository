from pathlib import Path

from homework9.task3 import universal_file_counter

file_extension = "txt"
test_dir = Path("tests/homework9/test_dir")
tokenizer = str.split


def test_count_lines():
    """Testing that without tokenizer function returns sum of number of lines in
    all files with specified file extension from directory."""
    num_of_lines = universal_file_counter(test_dir, file_extension)
    assert num_of_lines == 8


def test_count_tokens():
    """Testing that with tokenizer str.split function returns sum of number of
    tokens in all files with specified file extension from directory."""
    num_of_tokens = universal_file_counter(test_dir, file_extension, tokenizer)
    assert num_of_tokens == 11
