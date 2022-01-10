from homework3.task3 import make_filter

SAMPLE_DATA = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }
]


def test_find_dict_with_filter():
    """Testing that filter finds entrance with specified keyword arguments."""
    assert make_filter(name='polly', type='bird').apply(SAMPLE_DATA) == \
           [{'is_dead': True,
             'kind': 'parrot',
             'type': 'bird',
             'name': 'polly'}]


def test_find_no_dict_with_filter():
    """Testing that filter cannot find entrance with specified keyword
    arguments if there are no such dict in provided data."""
    assert not make_filter(name='qwerty', type='bird').apply(SAMPLE_DATA)
