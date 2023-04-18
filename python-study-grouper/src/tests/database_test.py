import unittest
import sys
import os
import sqlite3
from dotenv import load_dotenv

new_path = os.path.dirname((__file__)) + "/../"
sys.path.append(new_path)

import initialize_database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        initialize_database.initialize_database()

        dir = os.path.dirname(__file__)+"/../../"
        load_dotenv(dotenv_path=dir + ".env.test")
        self.DATABASE_NAME = os.getenv("TEST_DATABASE") or "test-db.sqlite3"
        self.connection = sqlite3.connect(self.DATABASE_NAME)
        self.connection.isolation_level = None

        initialize_database.drop_all_tables(self.connection)


    def test_create_ungrouped_table(self):
        initialize_database.create_ungrouped_table(self.connection)
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT name 
            FROM sqlite_master 
            WHERE type='table';
        """)
        self.assertEqual(cursor.fetchall(), [("Ungrouped",)])

    def test_drop_tables(self):
        initialize_database.drop_all_tables(self.connection)
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT name 
            FROM sqlite_master 
            WHERE type='table';
        """)
        self.assertEqual(cursor.fetchall(), [])

    def test_create_courses_table(self):
        initialize_database.create_courses_table(self.connection)
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT name 
            FROM sqlite_master 
            WHERE type='table';
        """)
        self.assertEqual(cursor.fetchall(), [("Courses",)])

    def test_add_course(self):
        initialize_database.create_courses_table(self.connection)
        initialize_database.add_course(self.connection, "Test course")
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT course_name
            FROM Courses 
            WHERE course_name = 'Test course';
        """)
        self.assertEqual(cursor.fetchall(), [("Test course",)])

    def test_get_courses(self):
        initialize_database.create_courses_table(self.connection)
        initialize_database.add_course(self.connection, "Test course")
        initialize_database.add_course(self.connection, "Test course 2")
        self.assertEqual(initialize_database.get_courses(self.connection), [("Test course",), ("Test course 2",)])