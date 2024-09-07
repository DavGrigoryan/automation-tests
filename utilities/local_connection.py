import pymysql
from pymysql.cursors import DictCursor
from pymysql import MySQLError
from contextlib import contextmanager
from utilities.config import config

@contextmanager
def get_local_db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host=config('DB_HOST'),
            port=int(config('DB_PORT')),
            database=config('DB_DATABASE'),
            user=config('DB_USERNAME'),
            password=config('DB_PASSWORD'),
            cursorclass=DictCursor
        )
        yield conn
    except MySQLError as e:
        print(f"Local database connection failed: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
