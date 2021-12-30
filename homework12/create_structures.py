from typing import List

from sqlalchemy import Table

from homework12.classes import BASE
from homework12.orm import engine


def create_tables() -> List[Table]:
    """
    Create tables in database for all classes
    :return: List of created tables
    """
    tables = BASE.metadata.sorted_tables
    with engine.connect():
        BASE.metadata.create_all(engine)
    return tables


def delete_tables(tables: List[Table]):
    """
    Delete specified tables
    :param tables: List of tables
    """
    with engine.connect():
        BASE.metadata.drop_all(engine, tables, checkfirst=True)


if __name__ == "__main__":
    tbls = create_tables()
    # delete_tables(tbls)
