from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Homework(Base):
    __tablename__ = "homeworks"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    deadline = Column(DateTime)
    created = Column(DateTime, default=datetime.now)


class HomeworkResult(Base):
    __tablename__ = "homeworks_results"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    homework_id = Column(Integer, ForeignKey("homeworks.id"), nullable=False)
    solution = Column(String)
    created = Column(DateTime, default=datetime.now)


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
