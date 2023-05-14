import sqlite3
import initialize_database

def _initialize_database():
    initialize_database.initialize_database()

def _add_course(connection, course_name):
    add = _row_exists(
        connection, table_name="Courses", 
        column_name="course_name", 
        column_value=course_name)
    
    if add:
        cursor = connection.cursor()
        cursor.execute(f"""
            INSERT INTO Courses 
                (course_name) 
                VALUES ('{course_name}');
        """)
        print(f"Course {course_name} added to database")
        return cursor.lastrowid
    return _get_course_id(connection, course_name)

def _row_exists(connection, table_name, column_name, column_value):
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT * 
        FROM {table_name} 
        WHERE {column_name} = '{column_value}';
    """)
    return cursor.fetchone() is None

def _add_ungrouped(connection, course_name, email):
    cursor = connection.cursor()
    cursor.execute(f"""
        INSERT INTO Ungrouped 
            (course_name, email) 
            VALUES ('{course_name}', '{email}');
    """)
    
def _get_ungrouped(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM Ungrouped;
    """)
    return cursor.fetchall()

def _remove_ungrouped(connection, table_id):
    cursor = connection.cursor()
    cursor.execute(f"""
        DELETE 
        FROM Ungrouped 
        WHERE id = {table_id};
    """)

def _get_courses(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT course_name
        FROM Courses;
    """)
    return cursor.fetchall()

def _get_ungrouped_by_courses(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT course_name, COUNT(*) 
        FROM Ungrouped 
        GROUP BY course_name;
    """)
    return cursor.fetchall()

def _get_course_id(connection, course):
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT id 
        FROM Courses 
        WHERE course_name = '{course}';
    """)
    return cursor.fetchone()[0]

def _get_ungrouped_by_course(connection, course_name):
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT id, email
        FROM Ungrouped
        WHERE course_name = '{course_name}';
    """)
    return cursor.fetchall()

def _add_new_group(connection, course_name):
    cursor = connection.cursor()
    cursor.execute(f"""
        INSERT INTO Groups
            (course_name)
            VALUES ('{course_name}');
    """)
    return cursor.lastrowid

def _get_groups(connection, course_name):
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT *
        FROM Groups
        WHERE course_name = '{course_name}';
    """)
    return cursor.fetchall()

def _get_amount_of_participants_in_group(connection, group_id):
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT COUNT(*)
        FROM Participants
        WHERE group_id = {group_id};
    """)
    return cursor.fetchone()[0]

def _get_members_of_group(connection, group_id):
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT *
        FROM Participants
        WHERE group_id = {group_id};
    """)
    return cursor.fetchall()

def _add_to_group(connection, group_id, email):
    cursor = connection.cursor()
    cursor.execute(f"""
        INSERT INTO Participants
            (group_id, email)
            VALUES ({group_id}, '{email}');
    """)

def _remove_from_group(connection, member_id):
    cursor = connection.cursor()
    cursor.execute(f"""
        DELETE FROM Participants
        WHERE id = {member_id};
    """)