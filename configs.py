import pymysql.cursors


class Db:
    def __init__(self):
        self.db = pymysql.Connection(host = '127.0.0.1',
                                     user = 'root',
                                     password = 'root',
                                     db = 'i1_home',
                                     charset = 'utf8mb4',
                                     cursorclass = pymysql.cursors.DictCursor)

    def __del__(self):
        self.db.close()

    def query(self, sql, *args):
        with self.db.cursor() as cursor:
            cursor.execute(sql, *args)
            return cursor.fetchall()
