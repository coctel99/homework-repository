import datetime
from collections import defaultdict

from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Interval,
                        String)
from sqlalchemy.orm import backref, declarative_base, relationship

MIN_SOLUTION_LEN = 5
Base = declarative_base()


class DeadlineError(Exception):
    print("You are late")


class Homework(Base):
    __tablename__ = "homeworks"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    text = Column(String)
    deadline = Column(Interval)
    created = Column(DateTime)
    homework_results = relationship("HomeworkResult",
                                    backref=backref("homeworks"))

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


class HomeworkResult(Base):
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


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student(User):
    __tablename__ = "students"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    homework_results = relationship("HomeworkResult",
                                    backref=backref("author"))
    __mapper_args__ = {
        "polymorphic_identity": "student",
    }

    def do_homework(self, homework: Homework, solution: str):
        """
        Return homework if it is active, else return None
        :rtype: object
        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError


class Teacher(User):
    __tablename__ = 'teachers'
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    homeworks = relationship("Homework",
                             backref=backref("author"))
    __mapper_args__ = {
        "polymorphic_identity": "teacher",
    }

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
