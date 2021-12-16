"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    print('You are late')


class Homework:
    def __init__(self, text, deadline, created):
        self.text = text
        self.deadline = deadline
        self.created = created

    def is_active(self) -> bool:
        """
        Checks if homework is active (deadline haven't passed)
        :return: Is homework active or not
        """
        return self.created + self.deadline > datetime.datetime.today()


class HomeworkResult:
    def __init__(self, author: "Student", homework: Homework,
                 solution: str):
        if type(homework) is not Homework:
            raise TypeError("Not a Homework object")
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.today()


class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student(User):
    def do_homework(self, homework: Homework, solution: str):
        """
        Return homework if it is active, else return None
        :rtype: object
        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError


class Teacher(User):
    homework_done = defaultdict(HomeworkResult)

    @staticmethod
    def create_homework(text, deadline):
        """
        Create new instance of Homework class
        :param text: Text of the homework
        :param deadline: Deadline of the homework
        :return: New Homework class instance
        """
        deadline = datetime.timedelta(days=deadline)
        created = datetime.datetime.today()
        return Homework(text, deadline, created)

    @staticmethod
    def check_homework(hw_result: HomeworkResult):
        """
        Check if homework solution length is correct

        If homework solution length is more than 5 it returns true
        and adds homework result to homework_done

        If homework solution length is less or equal 5 it returns False

        :param hw_result: Homework result to check
        :return: True if homework result solution is more than 5, else
        return false
        """
        if len(hw_result.solution) <= 5:
            return False

        Teacher.homework_done[hw_result.homework] = hw_result
        return True

    @staticmethod
    def reset_results(homework: Homework = None):
        """
        Resets done homework results

        If no arguments passed: Clear all homework done

        If Homework is passed: Remove specific homework from dict
        :param homework: Homework to remove
        """
        Teacher.homework_done.pop(homework, None) if \
            homework else Teacher.homework_done.clear()
