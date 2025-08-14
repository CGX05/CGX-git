import pymysql

def sql_db():
    return pymysql.connect(
        host='8.134.127.43',
        port=3306,
        user='cgx',
        password='CGx2005214.',
        database='BLOG',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
# print(sql_db().get_server_info())