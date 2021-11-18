from homework2.task1 import (count_non_ascii_chars, count_punctuation_chars,
                             get_longest_diverse_words,
                             get_most_common_non_ascii_char, get_rarest_char)


def test_longest_diverse_words():
    """Testing that get_longest_diverse_words function gives correct result
    on text"""
    assert get_longest_diverse_words(
        "./tests/homework2/data.txt") == ['Bevölkerungsabschub,',
                                          'Kollektivschuldiger,',
                                          'Schicksalsfiguren;',
                                          'résistance-Bewegungen,',
                                          'unmißverständliche',
                                          'Entscheidungsschlacht.',
                                          'Gewissenserforschung,',
                                          'Machtbewußtsein,',
                                          'Schicksalsstunde,',
                                          'Schöpfungsmacht.']


def test_get_rarest_char():
    """Testing that get_rarest_char function gives correct result on text"""
    assert get_rarest_char("./tests/homework2/data.txt") == "›"


def test_count_punctuation_chars():
    """Testing that count_punctuation_chars function gives correct result
    on text"""
    assert count_punctuation_chars("./tests/homework2/data.txt") == 4456


def test_count_non_ascii_chars():
    """Testing that count_non_ascii_chars function gives correct result on
    text"""
    assert count_non_ascii_chars("./tests/homework2/data.txt") == 2972


def test_get_most_common_non_ascii_char():
    """Testing that get_most_common_non_ascii_char function gives correct
    result on text"""
    assert get_most_common_non_ascii_char(
        "./tests/homework2/data.txt") == "ä"
