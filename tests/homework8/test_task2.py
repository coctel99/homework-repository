import sqlite3

import pytest

from homework8.task2 import TableData

TEST_DB = './tests/homework8/test.sqlite'
TEST_TABLE = 'presidents'
TEST_ORIG_INIT_PARAM = 'Sasha'


def test_get_len():
    """Testing that len() method gives us number of data rows."""
    presidents = TableData(TEST_DB, TEST_TABLE)
    assert len(presidents) == 3


def test_get_updated_len():
    """Testing that len() method gives us number of data rows."""
    presidents = TableData(TEST_DB, TEST_TABLE)
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute(f"insert into {TEST_TABLE} (name, age, country) "
                   f"values ('Putin', 10000, 'Russia')")
    conn.commit()
    assert len(presidents) == 4
    cursor.execute(f"delete from {TEST_TABLE} where name = 'Putin'")
    conn.commit()


def test_get_data_row():
    """Testing that data row can be got using '[]'."""
    presidents = TableData(TEST_DB, TEST_TABLE)
    assert presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')


def test_get_unexisting_data_row():
    """Testing that ValueError is risen."""
    presidents = TableData(TEST_DB, TEST_TABLE)
    with pytest.raises(ValueError):
        _ = presidents['Barabanov']


def test_get_updated_data_row():
    """Testing that data row is being added from the database."""
    presidents = TableData(TEST_DB, TEST_TABLE)
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute(f"insert into {TEST_TABLE} (name, age, country) "
                   f"values ('Putin', 10000, 'Russia')")
    conn.commit()
    assert presidents['Putin'] == ('Putin', 10000, 'Russia')
    cursor.execute(f"delete from {TEST_TABLE} where name = 'Putin'")
    conn.commit()


def test_check_if_exists():
    """Testing that __contains__ method gives True if specified key exists."""
    presidents = TableData(TEST_DB, TEST_TABLE)
    assert 'Yeltsin' in presidents


def test_check_if_not_exists():
    """Testing that __contains__ method gives False if specified key dont't
     exist."""
    presidents = TableData(TEST_DB, TEST_TABLE)
    assert 'Barabanov' not in presidents


def test_iterate():
    """Testing that class values can be iterated through."""
    presidents = TableData(TEST_DB, TEST_TABLE)

    list_of_presidents = []
    for president in presidents:
        list_of_presidents.append(president)

    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * from {TEST_TABLE}')
    president_names = cursor.fetchall()

    assert president_names == list_of_presidents
