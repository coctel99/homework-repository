import os
from datetime import datetime, timedelta

import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from homework12.create_records import fill_tables_with_data
from homework12.create_structures import create_tables
from homework12.models import Homework, HomeworkResult, Student, Teacher, User
from homework12.orm import db_name


def test_if_tables_created():
    """Testing that all necessary tables are created."""
    create_tables()
    engine = create_engine(f"sqlite:///{db_name}")
    table_names = inspect(engine).get_table_names()
    assert table_names == ["homeworks", "homeworks_results",
                           "students", "teachers", "users"]


def test_if_values_filled():
    """Testing that each table has at least one record."""
    create_tables()
    fill_tables_with_data()

    engine = create_engine(f"sqlite:///{db_name}")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    homework_rows_num = session.query(Homework).count()
    homework_result__rows_num = session.query(HomeworkResult).count()
    student_rows_num = session.query(Student).count()
    teacher_rows_num = session.query(Teacher).count()
    user_rows_num = session.query(User).count()
    session.commit()
    session.close()
    assert all([homework_rows_num, homework_result__rows_num,
                student_rows_num, teacher_rows_num, user_rows_num])


def test_if_same_values():
    """Testing that db records are equal to instance attributes."""
    create_tables()
    engine = create_engine(f"sqlite:///{db_name}")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    student_first_name = "Roman"
    student_last_name = "Petrov"
    teacher_first_name = "Daniil"
    teacher_last_name = "Shadrin"
    hw_id = 1
    hw_text = "Homework text"
    hw_author_id = 1
    hw_result_text = "I have done this hw"

    records = [
        Student(first_name=student_first_name,
                last_name=student_last_name),
        Teacher(first_name=teacher_first_name,
                last_name=teacher_last_name),
        Homework(text=hw_text,
                 deadline=datetime.today().date() + timedelta(days=6)),
        HomeworkResult(author_id=hw_author_id, homework_id=hw_id,
                       solution=hw_result_text)
    ]
    session.add_all(records)
    session.commit()

    db_hw_result = session.query(HomeworkResult).first()
    db_hw_result_author_id = db_hw_result.author_id
    db_hw_result_text = db_hw_result.solution
    session.commit()
    session.close()

    assert (db_hw_result_author_id == 1
            and db_hw_result_text == hw_result_text)


@pytest.fixture(autouse=True, scope="function")
def cleanup_file():
    """Delete database file at the end of every test."""
    yield
    if os.path.exists(db_name):
        os.remove(db_name)
