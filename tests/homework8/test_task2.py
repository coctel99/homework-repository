import sqlite3

from homework8.task2 import make_a_collection

TEST_DB = './tests/homework8/test.sqlite'
TEST_TABLE = 'presidents'
TEST_ORIG_INIT_PARAM = 'Sasha'


@make_a_collection
class A:
    def __init__(self, name):
        self.name = name


def test_original_init():
    """Testing that __init__ of original function is not overwritten."""
    presidents = A(name=TEST_ORIG_INIT_PARAM,
                   database_name=TEST_DB,
                   table_name=TEST_TABLE)
    assert presidents.name == TEST_ORIG_INIT_PARAM


def test_get_len():
    """Testing that len() method gives us number of data rows."""
    presidents = A(name=TEST_ORIG_INIT_PARAM,
                   database_name=TEST_DB,
                   table_name=TEST_TABLE)
    assert len(presidents) == 3


def test_get_data_row():
    """Testing that data row can be got using '[]'."""
    presidents = A(name=TEST_ORIG_INIT_PARAM,
                   database_name=TEST_DB,
                   table_name=TEST_TABLE)
    assert presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')


def test_check_if_exists():
    """Testing that __contains__ method gives True if specified key exists."""
    presidents = A(name=TEST_ORIG_INIT_PARAM,
                   database_name=TEST_DB,
                   table_name=TEST_TABLE)
    assert 'Yeltsin' in presidents


def test_check_if_not_exists():
    """Testing that __contains__ method gives False if specified key dont't
     exist."""
    presidents = A(name=TEST_ORIG_INIT_PARAM,
                   database_name=TEST_DB,
                   table_name=TEST_TABLE)
    assert 'Barabanov' not in presidents


def test_iterate():
    """Testing that class values can be iterated through."""
    presidents = A(name=TEST_ORIG_INIT_PARAM,
                   database_name=TEST_DB,
                   table_name=TEST_TABLE)

    list_of_presidents = []
    for president in presidents:
        list_of_presidents.append(president)

    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * from {TEST_TABLE}')
    president_names = cursor.fetchall()

    assert president_names == list_of_presidents
