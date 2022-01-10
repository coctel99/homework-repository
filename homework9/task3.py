"""
Write a function that takes directory path, a file extension and an optional
tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6
"""
from pathlib import Path
from typing import Callable, Optional


def _count_lines(file_path: Path):
    with file_path.open() as fi:
        number_of_lines = 0
        for _ in fi:
            number_of_lines += 1
        return number_of_lines


def _count_tokens(file_path: Path, tokenizer: Optional[Callable]):
    with file_path.open() as fi:
        number_of_tokens = 0
        for line in fi:
            token = tokenizer(line)
            number_of_tokens += len(token)
        return number_of_tokens


def universal_file_counter(
        dir_path: Path,
        file_extension: str,
        tokenizer: Optional[Callable] = None
) -> int:
    files = [x for x in dir_path.glob(f"**/*.{file_extension}") if x.is_file()]
    if tokenizer:
        num_of_tokens = sum([_count_tokens(file, tokenizer) for file in files])
        return num_of_tokens
    num_of_lines = sum([_count_lines(file) for file in files])
    return num_of_lines
