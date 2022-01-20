from typing import List

from sqlalchemy import Table

from homework12.models import Base
from homework12.orm import engine


def create_tables() -> List[Table]:
    """
    Create tables in database for all classes
    :return: List of created tables
    """
    tables = Base.metadata.sorted_tables
    with engine.connect():
        Base.metadata.create_all(engine)
    return tables


def delete_tables(tables: List[Table]):
    """
    Delete specified tables
    :param tables: List of tables
    """
    with engine.connect():
        Base.metadata.drop_all(engine, tables, checkfirst=True)


if __name__ == "__main__":
    tbls = create_tables()
    # delete_tables(tbls)
