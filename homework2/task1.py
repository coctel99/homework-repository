"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file=file_path, mode="r", encoding="unicode-escape") as fi:
        unique_words = set()
        for line in fi:
            for word in line.strip().split():
                if word not in unique_words:
                    unique_words.update([word])
    fi.close()
    most_diverse = dict((x, len(set(x))) for x in unique_words)
    most_diverse = (sorted(sorted(most_diverse),
                           key=most_diverse.get,
                           reverse=True)[:10])
    return most_diverse


def get_rarest_char(file_path: str) -> str:
    with open(file=file_path, mode="r", encoding="unicode-escape") as fi:
        rarest = {}
        for line in fi:
            for char in list(line.strip()):
                if char not in rarest:
                    rarest[char] = 1
                else:
                    rarest[char] += 1
    fi.close()
    rarest = min(rarest, key=rarest.get)
    return rarest


def count_punctuation_chars(file_path: str) -> int:
    punct_chars_list = list(",.:;!?&*()[]{}\'\"<>«»—")
    punct_chars = 0
    with open(file=file_path, mode="r", encoding="unicode-escape") as fi:
        for line in fi:
            for char in list(line.strip()):
                if char in punct_chars_list:
                    punct_chars += 1
    fi.close()
    return punct_chars


def count_non_ascii_chars(file_path: str) -> int:
    non_ascii_chars = 0
    with open(file=file_path, mode="r", encoding="unicode-escape") as fi:
        for line in fi:
            for char in list(line.strip()):
                if len(str(char).encode("utf-8")) > 1:
                    non_ascii_chars += 1
    fi.close()
    return non_ascii_chars


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file=file_path, mode="r", encoding="unicode-escape") as fi:
        non_ascii_chars = {}
        for line in fi:
            for char in list(line.strip()):
                if len(str(char).encode("utf-8")) > 1:
                    if char not in non_ascii_chars:
                        non_ascii_chars[char] = 1
                    else:
                        non_ascii_chars[char] += 1
    fi.close()
    most_common = max(non_ascii_chars, key=non_ascii_chars.get)
    return most_common
