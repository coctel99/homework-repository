from typing import List

from sqlalchemy import Table, create_engine

from homework12.classes import Base

DB_NAME = "main.db"
ENGINE = create_engine(f"sqlite:///{DB_NAME}")


def create_tables() -> List[Table]:
    """
    Create tables in database for all classes
    :return: List of created tables
    """
    tables = Base.metadata.sorted_tables
    with ENGINE.connect():
        Base.metadata.create_all(ENGINE)
    return tables


def delete_tables(tables: List[Table]):
    """
    Delete specified tables
    :param tables: List of tables
    """
    with ENGINE.connect():
        Base.metadata.drop_all(ENGINE, tables, checkfirst=True)


if __name__ == '__main__':
    tbls = create_tables()
    # delete_tables(tbls)
