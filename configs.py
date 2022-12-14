import os

import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_STORE = os.getenv('DB_STORE', '')


class Db:
    def __init__(self):
        self.db = pymysql.Connection(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, db = DB_STORE,
                                     charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

    def __del__(self):
        self.db.close()

    def query(self, sql, *args):
        try:
            with self.db.cursor() as cursor:
                cursor.execute(sql, args)
                return cursor.fetchall()
        except Exception as e:
            print(str(e))
            return str(e)

    def exec(self, sql, *args):
        try:
            with self.db.cursor() as cursor:
                cursor.execute(sql, args)
            self.db.commit()
        except Exception as e:
            print(str(e))
            return str(e)
