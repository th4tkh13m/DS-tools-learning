"""
This module contains function to deal with database info.
"""

def get_info(file_path:str):
    """
    Get database info from file.

    The mentioned file must have the following format:
    `sql_type;username;password;host;dbname`.


    Returns:
        str: Type of SQL Management System
        str: Username of the SQL account
        str: password of the SQL account
        str: The host address of the SQL server
        str: The name of the database
    """
    with open(file_path, encoding="utf-8") as info_file:
        for line in info_file:
            sql_type, username, password, host, dbname = line.split(";")
    return sql_type, username, password, host, dbname
