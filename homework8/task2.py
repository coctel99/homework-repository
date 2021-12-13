import sqlite3
from typing import Iterator


def _create_connection(db):
    """Establish database connection."""
    conn = sqlite3.connect(db)
    return conn.cursor()


def make_a_collection(cls):
    """
    Make a database table data collection from specified class.

    Wrapper store database records in 'collection' dict. Dict keys
    are made from the first database table column, which is assumed
    to store a primary key. Dict values contain corresponding to key
    values data rows.

    :param cls: Class to decorate
    :return: Decorated class
    """
    class TableData:
        original_init = cls.__init__

        def __init__(self, database_name, table_name, *args, **kwargs):
            self.original_init(*args, **kwargs)
            self.collection = {}
            cursor = _create_connection(database_name)
            cursor.execute(f'SELECT * from {table_name}')
            while row := cursor.fetchone():
                # Assuming that table key column is the first one
                key = row[0]
                self.collection.update({key: row})

        def __iter__(self) -> Iterator:
            return iter(self.collection.values())

        def __contains__(self, item: object) -> bool:
            return True if item in self.collection else False

        def __len__(self) -> int:
            return len(self.collection)

        def __getitem__(self, item: object):
            return self.collection.get(item)

    return TableData
