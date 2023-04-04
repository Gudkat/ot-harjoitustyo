import sqlite3
from config import DATABASE_PATH

def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.isolation_level = None
    return connection