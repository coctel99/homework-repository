from homework12.classes import Student, Teacher
from homework12.orm import session


def fill_tables_with_data():
    student = Student("Roman", "Petrov")
    session.add(student)

    teacher = Teacher("Daniil", "Shadrin")
    session.add(teacher)

    homework = teacher.create_homework("text", 5)
    session.add(homework)

    homework_result = student.do_homework(homework, "I have done this hw")
    session.add(homework_result)

    teacher.check_homework(homework_result)
    session.commit()


if __name__ == "__main__":
    fill_tables_with_data()
