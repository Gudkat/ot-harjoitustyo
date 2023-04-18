# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code, and also in assistance with tkinter syntax

from os import path as os_path
from sys import path as sys_path

# importing modules is hard. Gotta go ask for help in ws to make this cleaner
new_path = os_path.dirname((__file__)) + "/../"
sys_path.append(new_path)

from database_connection import get_connection

import tkinter
from database_tools.database_commands import add_ungrouped

class FindGroupView:
    def __init__(self, root, back_button_functionality):
        self._root = root
        self._back_button_functionality = back_button_functionality
        self._initialize()

    def _initialize(self):
        self._root.title("Study grouper - Find Group")

    def _render(self):
        self._root.mainloop()

    def start(self):
        self._create_grid()
        self._render()

    def destroy(self):
        self._frame.destroy()
        self._frame = None

    def _create_grid(self):
        self._frame= tkinter.Frame(self._root, padx=20, pady=20)
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
        course_id = self._course_id_text_box.get()
        connection = get_connection()
        add_ungrouped(connection, course_id, email)

        print(f"{email} signed up for course: {course_id}")


# def run():
#     view = FindGroupView()
#     view._create_grid()
#     view._render()


if __name__ == "__main__":
    conn = get_connection()
    add_ungrouped(conn, "TKT123", "esimerkki@domain.com")