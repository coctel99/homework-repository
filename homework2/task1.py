"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from dataclasses import dataclass, asdict
from typing import List, TextIO
from unicodedata import category

NUMBER_OF_DIVERSE_WORDS = 10


@dataclass
class TextReader:
    most_diverse: List
    rarest_char: str
    punct_chars_number: int
    non_ascii_chars_number: int
    non_ascii_chars_most_common: str


def get_next_char(file: TextIO) -> str:
    """
    Read next character from file
    :param file: Opened file
    """
    while True:
        char = file.read(1)
        if not char:
            break
        yield char


def read_file(file_path: str) -> type(TextReader):
    """
    Read file and get 5 values:
    1) 10 longest words consisting from largest amount of unique symbols
    2) The rarest symbol for document
    3) Number of punctuation chars
    4) Number of non ascii chars
    5) The most common non ascii char for document
    :param file_path: Path to the file to read
    :return: Tuple of with 5 counted values
    """
    with open(file_path, encoding="unicode-escape", errors="ignore") as file:
        word = ""
        unique_words = {}
        rarest_chars = {}
        punct_chars_number = 0
        ascii_chars = string.printable
        non_ascii_chars = {}
        for char in get_next_char(file):
            # If character is a unicode Letter character
            if category(char).startswith("L"):
                word += char
            else:
                if word:
                    if word not in unique_words:
                        unique_words.update({word: len(set(word))})
                    word = ""
            rarest_chars[char] = rarest_chars.get(char, 0) + 1
            if category(char).startswith("P"):
                punct_chars_number += 1
            if char not in ascii_chars:
                non_ascii_chars[char] = non_ascii_chars.get(char, 0) + 1
            pass
        most_diverse = sorted(unique_words, key=unique_words.get,
                              reverse=True)
        TextReader.most_diverse = most_diverse[:NUMBER_OF_DIVERSE_WORDS]
        TextReader.rarest_char = min(rarest_chars, key=rarest_chars.get)
        TextReader.punct_chars_number = punct_chars_number
        TextReader.non_ascii_chars_number = sum(non_ascii_chars.values())
        TextReader.non_ascii_chars_most_common = max(non_ascii_chars,
                                                     key=non_ascii_chars.get)
        return TextReader
