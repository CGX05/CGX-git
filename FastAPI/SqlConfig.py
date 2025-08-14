import pymysql

def sql_config():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        db="a",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )