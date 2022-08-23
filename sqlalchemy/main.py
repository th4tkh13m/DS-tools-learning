"""
Execute SQLAlchemy scripts.
"""
from db_connect import connect
from classes import person
from sqlalchemy import text
from sqlalchemy.orm import Session
from datetime import date

def main():
    """
    This function is the main function use to execute scripts.
    """
    engine = connect("supplementals/dbinfo.txt")
    student_one = person.Student("DE160000", "Khiem", "M", date(2002,1,1), "SE")

    person.Base.metadata.create_all(engine)
    with Session(engine) as session:
        session.add(student_one)
        session.commit()
    

if __name__ == "__main__":
    main()
