# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code and for checking tkinter syntax

import tkinter
from database_connection import get_connection
from database_tools.database_commands import _get_ungrouped_by_courses, _get_course_id, _get_courses

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
        self._frame= tkinter.Frame(self._root, borderwidth=2, padx=20, pady=20)
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)
        self._frame.grid(row=0, column=0, sticky="nsew")
        self._frame.grid_columnconfigure(0, weight=1, minsize=200)


    def _pack(self):
        self._frame.pack(fill="x", expand=True, side="bottom")

    def _create_button(self, text, row, column):
        button = tkinter.Button(self._frame, text=text, command=lambda: self._handle_button_click(text))
        button.grid(row=row, column=column, sticky="ew")

    def _create_courses_buttons(self, courses):
        for i in range(len(courses)):
            self._create_button(courses[i][0], row=i, column=0)

    def _create_ungrouped_amount_labels(self, courses):
        for i in range(len(courses)):
            self._create_label(courses[i][1], row=i)

    def _create_label(self, text, row, column=1):
        label = tkinter.Label(self._frame, text=text)
        label.grid(row=row, column=column, sticky="ew")

    def _handle_button_click(self, course_id):
        self._handle_add_to_group_button(course_id)

    def _create_grid(self):
        self._create_back_button()
        self._create_title_row()
        self._create_rows()
        self._frame.columnconfigure(1, minsize=25)

    def _create_rows(self):
        conn = get_connection()
        courses = _get_courses(conn)
        ungrouped_by_courses = _get_ungrouped_by_courses(conn)
        for i in range(len(courses)):
            self._create_course_button(i+2, courses[i][0])
            found = False
            for course in ungrouped_by_courses:
                if course[0] == courses[i][0]:
                    self._create_ungrouped_amount_label(i+2, course[1])
                    found = True
                    break
            if not found:
                self._create_ungrouped_amount_label(i+2, 0)

    def _create_title_row(self):
        self._create_label(text="Courses", row=1, column=0)
        self._create_label("Ungrouped", row=1, column=1)

    def _create_course_button(self, row, course_id):
        button = tkinter.Button(self._frame, text=course_id, command=lambda: self._handle_button_click(course_id))
        button.grid(row=row, column=0, sticky="ew")

    def _create_ungrouped_amount_label(self, row, amount):
        label = tkinter.Label(self._frame, text=amount)
        label.grid(row=row, column=1, sticky="ew")

    def _create_back_button(self):
        button = tkinter.Button(
            self._frame, 
            text="Back", 
            command=self._handle_back_button
        )
        button.grid(
            row=0,
            column=0, 
            columnspan=2, 
            sticky="ew",
            pady=(0, 10)
        )