import datetime

import pytest

from homework6.task2 import (DeadlineError, Homework, HomeworkResult, Student,
                             Teacher)


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


def test_do_active_homework():
    """Testing that active homework returns HomeworkResult instance."""
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    homework = teacher.create_homework("text", 5)
    hw_result = student.do_homework(homework, "I have done this hw")
    assert isinstance(hw_result, HomeworkResult)


def test_do_expired_homework():
    """Testing that expired homework raises DeadlineError."""
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    homework = teacher.create_homework("text", 0)
    with pytest.raises(DeadlineError):
        student.do_homework(homework, "I have done this hw")


def test_do_not_a_homework():
    """Testing that expired homework raises DeadlineError."""
    student = Student("Roman", "Petrov")
    with pytest.raises(TypeError) as err:
        _ = HomeworkResult(student, "fff", "Solution")
    assert "Not a Homework object" in str(err.value)


def test_check_correct_homework():
    """Testing that correct homework gives True."""
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    homework = teacher.create_homework("text", 5)
    hw_result = student.do_homework(homework, "I have done this hw")
    assert teacher.check_homework(hw_result)


def test_check_incorrect_homework():
    """Testing that incorrect homework gives False."""
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    homework = teacher.create_homework("text", 5)
    hw_result = student.do_homework(homework, "Hw")
    assert not teacher.check_homework(hw_result)


def test_multiple_teachers_check_one_homework():
    """Testing that each homework result is stored only once."""
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)

    result_1 = student.do_homework(oop_hw, "I have done this hw")

    opp_teacher.check_homework(result_1)
    homework_done_copy1 = opp_teacher.homework_done.copy()

    advanced_python_teacher.check_homework(result_1)
    homework_done_copy2 = advanced_python_teacher.homework_done.copy()

    assert homework_done_copy1 == homework_done_copy2


def test_multiple_teachers_share_storage_for_checked_homework():
    """Testing that homework results are stored in common storage."""
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    hw_result_1 = student.do_homework(oop_hw, "I have done this hw")
    hw_result_2 = student.do_homework(docs_hw, "I have done this hw too")

    opp_teacher.check_homework(hw_result_1)
    advanced_python_teacher.check_homework(hw_result_2)
    assert Teacher.homework_done.get(oop_hw) and \
           Teacher.homework_done.get(docs_hw)


def test_reset_all_results():
    """Testing that all homework results are deleted."""
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Lev", "Sokolov")
    oop_hw = teacher.create_homework("Learn OOP", 1)
    docs_hw = teacher.create_homework("Read docs", 5)
    hw_result_1 = student.do_homework(oop_hw, "I have done this hw")
    hw_result_2 = student.do_homework(docs_hw, "I have done this hw too")
    teacher.check_homework(hw_result_1)
    teacher.check_homework(hw_result_2)
    Teacher.reset_results()
    assert not Teacher.homework_done


def test_reset_specific_result():
    """Testing that one specific homework result is deleted."""
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Lev", "Sokolov")
    oop_hw = teacher.create_homework("Learn OOP", 1)
    docs_hw = teacher.create_homework("Read docs", 5)
    hw_result_1 = student.do_homework(oop_hw, "I have done this hw")
    hw_result_2 = student.do_homework(docs_hw, "I have done this hw too")
    teacher.check_homework(hw_result_1)
    teacher.check_homework(hw_result_2)
    Teacher.reset_results(oop_hw)
    assert not Teacher.homework_done.get(oop_hw) and \
           Teacher.homework_done.get(docs_hw)
