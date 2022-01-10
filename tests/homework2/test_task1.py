from homework2.task1 import read_file

TEXT_FILE = read_file("./tests/homework2/data.txt")


def test_longest_diverse_words():
    """Testing that get_longest_diverse_words function gives correct result
    on text"""
    assert TEXT_FILE.most_diverse == ['unmißverständliche',
                                      'Bevölkerungsabschub',
                                      'Kollektivschuldiger',
                                      'Werkstättenlandschaft',
                                      'Schicksalsfiguren',
                                      'Selbstverständlich',
                                      'Fingerabdrucks',
                                      'Friedensabstimmung',
                                      'außenpolitisch',
                                      'Seinsverdichtungen']


def test_get_rarest_char():
    """Testing that get_rarest_char function gives correct result on text"""
    assert TEXT_FILE.rarest_char == "›"


def test_count_punctuation_chars():
    """Testing that count_punctuation_chars function gives correct result
    on text"""
    assert TEXT_FILE.punct_chars_number == 5475


def test_count_non_ascii_chars():
    """Testing that count_non_ascii_chars function gives correct result on
    text"""
    assert TEXT_FILE.non_ascii_chars_number == 2972


def test_get_most_common_non_ascii_char():
    """Testing that get_most_common_non_ascii_char function gives correct
    result on text"""
    assert TEXT_FILE.non_ascii_chars_most_common == "ä"
