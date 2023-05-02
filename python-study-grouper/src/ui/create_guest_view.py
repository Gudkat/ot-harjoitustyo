# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code, and also in assistance with tkinter syntax

import tkinter
from database_connection import get_connection
from database_tools.database_commands import _add_ungrouped, _add_course

class FindGroupView:
    def __init__(self, root: tkinter.Tk, back_button_functionality):
        self._root = root
        self._frame = None
        self._back_button_functionality = back_button_functionality
        self._initialize()

    def _initialize(self):
        self._root.title("Study grouper - Find Group")

    def start(self):
        self._create_frame()
        self._create_grid()

    def destroy(self):
        self._frame.destroy()
        self._frame = None

    def _create_frame(self):
        if self._frame:
            self.destroy()
        self._frame= tkinter.Frame(self._root, padx=20, pady=20)

    def _create_grid(self):
        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_rowconfigure(1, weight=1)
        self._create_back_button()
        self._create_guest_button()
        self._create_label("Course id", 2)
        self._create_label("Email address", 3)

        self._create_course_id_tb()
        self._create_email_tb()

        self._frame.pack()

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
            sticky="ew"
        )

    def _create_guest_button(self):
        button = tkinter.Button(
            self._frame, 
            text="Sign up", 
            height=14, 
            command=self._handle_sign_up_button
        )
        button.grid(pady=(2,2))
        button.grid(row=1, column=0, columnspan=2, sticky="ew")

    def _create_course_id_tb(self):
        self._course_id_text_box = tkinter.Entry(self._frame)
        self._course_id_text_box.grid(row=2, column=1, sticky="ew")

    def _create_email_tb(self):
        self._email_text_box = tkinter.Entry(self._frame)
        self._email_text_box.grid(row=3, column=1, sticky="ew")

    def _create_label(self, text, row):
        label = tkinter.Label(self._frame, text=text)
        label.grid(row=row, column=0, sticky="w", padx=20, pady=1)

    def _get_email(self):
        return self._email_text_box.get()
    
    def _handle_back_button(self):
        self._back_button_functionality()        

    def _handle_sign_up_button(self):
        email = self._get_email()
        course_name = self._course_id_text_box.get()
        connection = get_connection()
        _add_course(connection, course_name)
        _add_ungrouped(connection, course_name, email)
        print(f"{email} signed up for course: {course_name}")
