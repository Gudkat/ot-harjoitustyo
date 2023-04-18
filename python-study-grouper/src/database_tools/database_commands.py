import sqlite3


def add_course(connection, course):
    connection.execute(f"""
        INSERT INTO Courses 
            (course_name) 
            VALUES ('{course}');
    """)

def add_ungrouped(connection, course_id, email):
    connection.execute(f"""
        INSERT INTO Ungrouped 
            (course_id, email) 
            VALUES ('{course_id}', '{email}');
    """)
    
def get_ungrouped(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            * 
            FROM Ungrouped;
    """)
    return cursor.fetchall()
