"""
This module handles connections to the database.
"""

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def connect(file_path:str) -> Engine:
    """
    Connect to a database given a database information file path.

    Args:
        file_path (str): The relative path of the database information file.

    Returns:
        Engine: The engine of the connection.
    """
    ## Get database information
    with open(file_path, encoding="utf-8") as info_file:
        for line in info_file:
            sql_type, username, password, host, dbname = line.split(";")

    ## Creating engine
    engine = create_engine(f"{sql_type}://{username}:{password}@{host}/{dbname}")

    ## Check if database exists, else create a new one with the given url
    if not database_exists(engine.url):
        create_database(engine.url)

    return engine
