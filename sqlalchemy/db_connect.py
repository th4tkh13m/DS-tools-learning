from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from db_info import get_info

sql_type, username, password, host, dbname = get_info()

## Creating engine
engine = create_engine(f"{sql_type}://{username}:{password}@{host}/{dbname}")

## Check if database exists, else create a new one with the given url
if not database_exists(engine.url):
    create_database(engine.url)