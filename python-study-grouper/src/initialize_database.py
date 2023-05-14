# git copilot has been used in creation of this file
from database_connection import get_connection


def initialize_database():
    connection = get_connection()
    drop_all_tables(connection)
    create_ungrouped_table(connection)
    create_courses_table(connection)
    create_groups_table(connection)
    create_participants_table(connection)
    return connection

def drop_all_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table';
    """)

    for table in cursor.fetchall():
        drop_table(connection, table[0])


def drop_table(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"""
        DROP TABLE IF EXISTS {table_name}
    """)


def create_ungrouped_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE Ungrouped (
            id INTEGER PRIMARY KEY, 
            course_name INT,
            email TEXT);
        """)


def create_courses_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY,
            course_name TEXT);
    """)


def add_course(connection, course):
    connection.execute(f"""
        INSERT INTO Courses 
            (course_name) 
            VALUES ('{course}');
    """)


def get_courses(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            course_name 
            FROM Courses;
    """)
    return cursor.fetchall()


def add_ungrouped(connection, course, email):
    connection.execute(f"""
        INSERT INTO Ungrouped 
            (course_name, email) 
            VALUES ('{course}', '{email}');
    """)

def get_course_id(connection, course):
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT 
            id 
            FROM Courses 
            WHERE course_name = '{course}';
    """)
    return cursor.fetcone()[0]


def get_ungrouped(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            * 
            FROM Ungrouped;
    """)
    return cursor.fetchall()


def remove_ungrouped(connection, table_id):
    cursor = connection.cursor()
    cursor.execute(f"""
        DELETE 
        FROM Ungrouped 
        WHERE id = {table_id};
    """)

def create_groups_table(connection):
    cursor = connection.cursor()
    cursor.execute(f"""
        CREATE TABLE Groups (
            id INTEGER PRIMARY KEY, 
            course_name TEXT)
    """)

def create_participants_table(connection):
    cursor = connection.cursor()
    cursor.execute(f"""
        CREATE TABLE Participants (
            id INTEGER PRIMARY KEY, 
            group_id INT, 
            email TEXT)
    """)
