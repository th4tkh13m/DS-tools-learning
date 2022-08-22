"""
This module contains all Person-related classes.

Includes:
- Student
- Teacher
"""

from datetime import date
from sqlalchemy.orm import registry, relationship
from sqlalchemy import Integer, Float, Date, String
from sqlalchemy import Column, ForeignKey, Identity, Table

registry_mapper = registry()
Base = registry_mapper.generate_base()

class Student(Base):
    __tablename__ = "Student"

    student_id = Column("id", String(8), primary_key=True)
    name = Column("name", String(30), nullable=False)
    gender = Column("gender", String(1))
    dob = Column("dob", Date)
    major = Column("major", String(2), nullable=False)

    attending = relationship("Attending", back_populates="student")

    def __init__(self, student_id:str, name:str, gender:str, dob:date, major:str) -> None:
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.dob = dob
        self.major = major

    def attend_class(self):
        pass

    def __repr__(self) -> str:
        return f"Student {self.name}, major {self.major}"

class Teacher(Base):
    __tablename__ = "Teacher"

    teacher_id = Column("id", String(8), primary_key=True)
    name = Column("name", String(30), nullable=False)
    gender = Column("gender", String(1))
    dob = Column("dob", Date)

    assigning = relationship("Assigning", back_populates="teacher")

    def __init__(self, teacher_id:str, name:str, gender:str, dob:date) -> None:
        self.teacher_id = teacher_id
        self.name = name
        self.gender = gender
        self.dob = dob

    def __repr__(self) -> str:
        return f"Teacher {self.name}"


    

