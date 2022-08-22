def get_info():
    with open("../supplementals/dbinfo.txt") as f:
        for line in f:
            sql_type, username, password, host, dbname = line.split(";")
    return sql_type, username, password, host, dbname