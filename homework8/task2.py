import sqlite3
from typing import Iterator


def _create_connection(db):
    """Establish database connection."""
    conn = sqlite3.connect(db)
    return conn.cursor()


def _get_db_value(db, table_name, name_value):
    """Update instance collection value with db value."""
    cursor = _create_connection(db)
    cursor.execute(f"SELECT * from {table_name} where name = '{name_value}'")
    return cursor.fetchone()


def _update_values_from_db(db, table_name):
    """Update all instance collection values."""
    cursor = _create_connection(db)
    cursor.execute(f"SELECT * from {table_name}")
    return cursor.fetchall()


class TableData:
    def __init__(self, database_name, table_name):
        self.collection = {}
        self.database_name = database_name
        self.table_name = table_name
        cursor = _create_connection(database_name)
        cursor.execute(f'SELECT * from {table_name}')
        while row := cursor.fetchone():
            # Assuming that table key column is the first one
            key = row[0]
            self.collection.update({key: row})

    def __iter__(self) -> Iterator:
        data = _update_values_from_db(self.database_name, self.table_name)
        for row in data:
            key = row[0]
            self.collection.update({key: row})
        return iter(self.collection.values())

    def __contains__(self, item: object) -> bool:
        cursor = _create_connection(self.database_name)
        cursor.execute(f"SELECT * from {self.table_name} where name ='{item}'")
        db_row = cursor.fetchone()
        return True if db_row else False

    def __len__(self) -> int:
        cursor = _create_connection(self.database_name)
        cursor.execute(f"SELECT count(*) from {self.table_name}")
        length = cursor.fetchone()[0]
        return length

    def __getitem__(self, item: object):
        # We don't have to update all collection if we need only one element
        val = _get_db_value(self.database_name, self.table_name, item)
        if not val:
            raise ValueError(f'{item} not in collection')
        self.collection.update({item: val})
        return self.collection.get(item)
