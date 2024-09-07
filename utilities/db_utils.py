from pymysql import MySQLError
from contextlib import contextmanager
from utilities.config import config
from pymysql.connections import Connection

# Import connection functions based on environment
if config('DB_CONNECTION') == 'local':
    from utilities.local_connection import get_local_db_connection as get_db_connection
else:
    from utilities.ssh_connection import get_ssh_db_connection as get_db_connection

from pymysql.cursors import Cursor, DictCursor


@contextmanager
def get_db_cursor(dict_cursor=True):
    with get_db_connection() as conn:
        assert isinstance(conn, Connection), "Expected a Connection object"
        if conn:
            cursor_type = DictCursor if dict_cursor else Cursor # TODO: Add support for non-dict cursor
            cursor = conn.cursor(cursor=cursor_type)
            try:
                yield cursor
                conn.commit()
            except MySQLError as e:
                print(f"Database operation failed: {e}")
                conn.rollback()
            finally:
                cursor.close()


def fetch_one(query, params=None):
    with get_db_cursor(dict_cursor=True) as cursor:
        cursor.execute(query, params)
        return cursor.fetchone()


def fetch_all(query, params=None):
    with get_db_cursor(dict_cursor=True) as cursor:
        cursor.execute(query, params)
        return cursor.fetchall()


def execute_query(query, params=None):
    with get_db_cursor(dict_cursor=False) as cursor:
        cursor.execute(query, params)
