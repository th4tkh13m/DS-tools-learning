"""
Execute SQLAlchemy scripts.
"""
from db_connect import connect
from sqlalchemy import text

def main():
    """
    This function is the main function use to execute scripts.
    """
    engine = connect("supplementals/dbinfo.txt")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 'hello'"))
        for row in result:
            print(row)

if __name__ == "__main__":
    main()
