import os

import pymysql.cursors
from dotenv import load_dotenv


class Db:
    def __init__(self):
        load_dotenv()
        self.db = pymysql.Connection(host = os.getenv("DB_HOST"),
                                     user = os.getenv("DB_USER"),
                                     password = os.getenv("DB_PASSWORD"),
                                     db = os.getenv("DB_STORE"),
                                     charset = 'utf8mb4',
                                     cursorclass = pymysql.cursors.DictCursor)

    def __del__(self):
        self.db.close()

    def query(self, sql, *args):
        with self.db.cursor() as cursor:
            cursor.execute(sql, *args)
            return cursor.fetchall()
