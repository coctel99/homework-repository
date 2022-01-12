import datetime
from collections import defaultdict

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, declarative_base, relationship

MIN_SOLUTION_LEN = 5
BASE = declarative_base()


class DeadlineError(Exception):
    pass


class Homework(BASE):
    __tablename__ = "homeworks"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    deadline = Column(DateTime)
    created = Column(DateTime)
    homework_results = relationship("HomeworkResult",
                                    backref=backref("homework"))

    def __init__(self, text, deadline, created):
        self.text = text
        self.deadline = deadline
        self.created = created

    def is_active(self) -> bool:
        """
        Checks if homework is active (deadline haven't passed)
        :return: Is homework active or not
        """
        return self.deadline > datetime.datetime.today()


class HomeworkResult(BASE):
    __tablename__ = "homeworks_results"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    homework_id = Column(Integer, ForeignKey("homeworks.id"), nullable=False)
    solution = Column(String)
    created = Column(DateTime)

    def __init__(self, author: "Student", homework: Homework,
                 solution: str):
        if type(homework) is not Homework:
            raise TypeError("Not a Homework object")
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.today()


class User(BASE):
    __abstract__ = True

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student(User):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    homework_results = relationship("HomeworkResult",
                                    backref=backref("author"))

    def do_homework(self, homework: Homework, solution: str):
        """
        Return homework if it is active, else return None
        :rtype: object
        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError("You are late!")


class Teacher(User):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    homework_done = defaultdict(HomeworkResult)

    @staticmethod
    def create_homework(text, deadline):
        """
        Create new instance of Homework class
        :param text: Text of the homework
        :param deadline: Deadline of the homework
        :return: New Homework class instance
        """
        created = datetime.datetime.now()
        deadline = created + datetime.timedelta(days=deadline)
        return Homework(text, deadline, created)

    @staticmethod
    def check_homework(hw_result: type(HomeworkResult)):
        """
        Check if homework solution length is correct
        If homework solution length is more than 5 it returns true
        and adds homework result to homework_done
        If homework solution length is less or equal 5 it returns False
        :param hw_result: Homework result to check
        :return: True if homework result solution is more than 5, else
        return false
        """
        if len(hw_result.solution) <= MIN_SOLUTION_LEN:
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
