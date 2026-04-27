import mysql.connector as sqltor
import config

_connection = None


def get_connection():
    global _connection
    if _connection is None or not _connection.is_connected():
        _connection = sqltor.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            passwd=config.DB_PASS,
            database=config.DB_NAME,
        )
    return _connection
