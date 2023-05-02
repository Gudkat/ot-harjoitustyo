# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code and for checking tkinter syntax

import tkinter
from database_connection import get_connection
from database_tools.database_commands import _get_ungrouped_by_courses, _get_course_id

class OverviewView:
    def __init__(self, root: tkinter.Tk, back_button_functionality, add_to_group_button_functionality):
        self._root = root
        self._frame = None
        self._handle_back_button = back_button_functionality
        self._handle_add_to_group_button = add_to_group_button_functionality
        self._initialize()

    def _initialize(self):
        self._root.title("Study grouper - Courses")

    def destroy(self):
        if self._frame:
            self._frame.destroy()
        self._frame = None

    def start(self):
        self._create_frame()
        self._create_grid()
        self._pack()

    def _create_frame(self):
        if self._frame:
            self.destroy()
        self._frame= tkinter.Frame(self._root, relief="sunken", borderwidth=2)
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)
        self._frame.grid(row=0, column=0, sticky="nsew")
        self._frame.grid_columnconfigure(0, weight=1, minsize=300)

    def _pack(self):
        self._frame.pack(fill="x", expand=True, side="left")

    def _create_button(self, text, row, column):
        button = tkinter.Button(self._frame, text=text, command=lambda: self._handle_button_click(text))
        button.grid(row=row, column=column, sticky="ew")

    def _create_courses_buttons(self, courses):
        for i in range(len(courses)):
            self._create_button(courses[i][0], row=i, column=0)

    def _create_ungrouped_amount_labels(self, courses):
        for i in range(len(courses)):
            self._create_label(courses[i][1], row=i)

    def _create_label(self, text, row):
        label = tkinter.Label(self._frame, text=text)
        label.grid(row=row, column=1, sticky="ew")

    def _handle_button_click(self, course_id):
        self._handle_add_to_group_button(course_id)

    def _create_grid(self):
        conn = get_connection()
        courses = _get_ungrouped_by_courses(conn)
        self._create_courses_buttons(courses)
        self._create_ungrouped_amount_labels(courses)
        self._frame.columnconfigure(1, minsize=25)
