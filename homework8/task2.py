import sqlite3
from typing import Iterator


class DBConnector(object):
    def __new__(cls, db):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnector, cls).__new__(cls)
        return cls.instance

    def __init__(self, db):
        conn = sqlite3.connect(db)
        self.cursor = conn.cursor()

    def get_db_value(self, table_name, name_value):
        """Get table value from database by name."""
        self.cursor.execute(f"SELECT * from {table_name} "
                            f"where name = '{name_value}'")
        return self.cursor.fetchone()

    def get_db_data(self, table_name):
        """Get all rows of specified table from database."""
        self.cursor.execute(f"SELECT * from {table_name}")
        return self.cursor.fetchall()

    def get_table_number_of_rows(self, table_name):
        """Get number of rows in the specified table."""
        self.cursor.execute(f"SELECT count(*) from {table_name}")
        return self.cursor.fetchone()[0]


class TableData:
    def __init__(self, database_name, table_name):
        self.conn = DBConnector(database_name)
        self.database_name = database_name
        self.table_name = table_name

    @property
    def collection(self):
        data = self.conn.get_db_data(self.table_name)
        return data

    def __iter__(self) -> Iterator:
        return iter(self.collection)

    def __contains__(self, item: object) -> bool:
        db_row = self.conn.get_db_value(self.table_name, item)
        return True if db_row else False

    def __len__(self) -> int:
        length = self.conn.get_table_number_of_rows(self.table_name)
        return length

    def __getitem__(self, item: object):
        # We don't have to update all collection if we need only one element
        val = self.conn.get_db_value(self.table_name, item)
        if not val:
            raise ValueError(f'{item} not in collection')
        return val
