import warnings
from cryptography.utils import CryptographyDeprecationWarning

# Suppress CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

from contextlib import contextmanager
from sshtunnel import SSHTunnelForwarder
import pymysql
from pymysql.cursors import DictCursor
from pymysql import MySQLError
from utilities.config import config


@contextmanager
def create_ssh_tunnel():
    tunnel = None
    try:
        tunnel = SSHTunnelForwarder(
            (config('SSH_HOST'), int(config('SSH_PORT'))),
            ssh_username=config('SSH_USER'),
            ssh_password=config('SSH_PASSWORD'),
            remote_bind_address=(config('DB_HOST'), int(config('DB_PORT'))),
            allow_agent=False,
        )
        tunnel.start()
        yield tunnel
    except Exception as e:
        print(f"SSH Tunnel creation failed: {e}")
    finally:
        if tunnel:
            tunnel.stop()


@contextmanager
def get_ssh_db_connection():
    conn = None
    try:
        with create_ssh_tunnel() as tunnel:
            conn = pymysql.connect(
                host='127.0.0.1',
                user=config('DB_USERNAME'),
                password=config('DB_PASSWORD'),
                database=config('DB_DATABASE'),
                port=tunnel.local_bind_port,
                cursorclass=DictCursor
            )
            yield conn
    except MySQLError as e:
        print(f"SSH database connection failed: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
