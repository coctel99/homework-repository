from datetime import datetime, timedelta

from homework12.models import Student, Teacher, Homework, HomeworkResult
from homework12.orm import session


def fill_tables_with_data():
    records = [
        Student(first_name="Roman", last_name="Petrov"),
        Teacher(first_name="Daniil", last_name="Shadrin"),
        Homework(text="text",
                 deadline=datetime.today().date() + timedelta(days=6)),
        HomeworkResult(author_id=1, homework_id=1,
                       solution="I have done this hw.")
    ]
    session.add_all(records)
    session.commit()


if __name__ == "__main__":
    fill_tables_with_data()
