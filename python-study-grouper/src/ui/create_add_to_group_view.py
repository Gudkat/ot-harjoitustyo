# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code and for checking tkinter syntax

import tkinter
from database_connection import get_connection
from database_tools.database_commands import _get_groups, _add_new_group, _get_amount_of_participants_in_group

class AddToGroupView:
    def __init__(self, root: tkinter.Tk, course_name, back_button_functionality, add_button_functionality):
        self._root = root
        self._frame = None
        self._course_name = course_name
        self._initialize()
        self._back_button_functionality = back_button_functionality
        self._handle_add_button = add_button_functionality

    def _initialize(self):
        self._root.title("Study grouper - Add participants to group")

    def destroy(self):
        self._frame.destroy()
        self._frame = None

    def start(self):
        self._create_frame()
        self._create_grid()
        self._pack()

    def _create_frame(self):
        if self._frame:
            self.destroy()
        self._frame = tkinter.Frame(self._root, borderwidth=2, padx=20, pady=20)

    def _pack(self):
        self._frame.pack(fill="both", expand=True, side="left")

    def _create_grid(self):
        conn = get_connection()
        groups = _get_groups(conn, self._course_name)
        self._create_title()
        self._create_back_button()
        self._create_create_new_group_button()
        for i in range(len(groups)):
            how_many = _get_amount_of_participants_in_group(conn, groups[i][0])
            self._create_label(row=i+3, column=0, text="Amount of participants in group: " + str(how_many))
            self._create_button(row=i+3, column=1, text="Add", group_id=groups[i][0])
 
    def _create_back_button(self):
        button = tkinter.Button(
            self._frame, 
            text="Back", 
            command=self._handle_back_button
        )
        button.grid(
            row=1,
            column=0, 
            columnspan=2, 
            sticky="ew"
        )

    def _create_title(self):
        title = tkinter.Label(self._frame, text=f"Groups for course {self._course_name}", font=('Arial', 16))
        title.grid(row=0, column=0, sticky="new", columnspan=2)

    def _create_create_new_group_button(self):
        button = tkinter.Button(self._frame, text="Create new group", command=self._handle_new_group_button_click)
        button.grid(row=2, column=0, sticky="ew", columnspan=2)        

    def _handle_back_button(self):
        self._back_button_functionality()

    def _handle_add_button_click(self, group_id):
        self._handle_add_button(self._course_name, group_id)

    def _handle_new_group_button_click(self):
        conn = get_connection()
        _add_new_group(conn, self._course_name)
        print("new group added")
        self.start()

    def _create_button(self, row, column, text, group_id):
        button = tkinter.Button(self._frame, text=text, command=lambda: self._handle_add_button_click(group_id))
        button.grid(row=row, column=column, sticky="ew")

    def _create_label(self, row, column=0, text=""):
        label = tkinter.Label(self._frame, text=text)
        label.grid(row=row, column=column, sticky="ew")