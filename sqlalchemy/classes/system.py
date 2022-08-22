"""
This module contains all System-related classes.

Includes:
- Subject
- Class
- Attending (Student attends to Class)
- Assigning (Teacher assigns to Class)
"""

from sqlalchemy.orm import registry, relationship
from sqlalchemy import Integer, Float, Date, String
from sqlalchemy import Column, ForeignKey, Identity, Table

registry_mapper = registry()
Base = registry_mapper.generate_base()

class Class(Base):
    __tablename__ = "Class"

    class_id = Column("id", Integer, Identity(), primary_key=True)
    name = Column("name", String(4), nullable=False)
    subject_id = Column("subject_id", ForeignKey("Subject.id"), nullable=False)
    semester = Column("semester", String(4), nullable=False)

    subject = relationship("Subject", back_populates="uni_class")

    def __init__(self, name:str, subject_id:str, semester:str) -> None:
        self.name = name
        self.subject_id = subject_id
        self.semester = semester

    def __repr__(self) -> str:
        return f"Class {self.name}, subject {self.subject.name}, semester {self.semester}"

class Subject(Base):
    __tablename__ = "Subject"

    subject_id = Column("id", String(6), primary_key=True)
    name = Column("name", String(50), nullable=False)

    uni_class = relationship("Subject", back_populates="subject")

    def __init__(self, subject_id:str, name:str) -> None:
        self.subject_id = subject_id
        self.name = name

    def __repr__(self) -> str:
        return f"Subject {self.subject_id}, name {self.name}"