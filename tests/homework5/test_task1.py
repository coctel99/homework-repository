import datetime

from homework5.task1 import Homework, Student, Teacher


def test_initialize_homework():
    """Testing that Homework instance is initialized with specified
    attributes."""
    homework = Homework(text="some text",
                        deadline=datetime.timedelta(days=5),
                        created=datetime.datetime(2021, 11, 29, 18, 0, 0))
    assert homework.text == "some text" and \
           homework.deadline == datetime.timedelta(days=5) and \
           homework.created == datetime.datetime(2021, 11, 29, 18, 0, 0)


def test_initialize_student():
    """Testing that Student instance is initialized with specified
    attributes."""
    student = Student("Roman", "Petrov")
    assert student.first_name == "Roman" and \
           student.last_name == "Petrov"


def test_initialize_teacher():
    """Testing that Teacher instance is initialized with specified
    attributes."""
    teacher = Teacher("Daniil", "Shadrin")
    assert teacher.first_name == "Daniil" and \
           teacher.last_name == "Shadrin"


def test_active_homework():
    """Testing that active homework returns itself."""
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    homework = teacher.create_homework("text", 5)
    assert student.do_homework(homework) is homework


def test_expired_homework():
    """Testing that expired homework returns None."""
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    homework = teacher.create_homework("text", 0)
    assert student.do_homework(homework) is None
