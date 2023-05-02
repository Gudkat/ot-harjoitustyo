# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code and for checking tkinter syntax

import tkinter
from database_connection import get_connection
from database_tools.database_commands import _get_groups, _add_new_group

class GroupsView:
    def __init__(self, root: tkinter.Tk, back_button_functionality, course_name ):
        self._root = root
        self._back_button_functionality = back_button_functionality
        self._course_name = course_name
        self._initialize()

    def _initialize(self):
        self._root.title(f"Study grouper - Groups for {self._course_name} Course")

    def _destroy(self):
        self._frame.destroy()
        self._frame = None

    def _create_frame(self):
        if self._frame:
            self._destroy()
        self._frame= tkinter.Frame(self._root, relief="sunken", borderwidth=2)

    def _pack(self):
        self._frame.pack(fill="x", expand=True, side="left")

    def _create_grid(self):
        conn = get_connection()
        self._groups = _get_groups(conn, self._course_name)
        self._create_button("Back", 0, 0)
        self._create_group_buttons()

    def _create_add_new_group_button(self):
        button = tkinter.Button(self._frame, text="Add new group", command=lambda: self._add_new_group_functionality())
        button.grid(row=0, column=1, sticky="ew")

    def _add_new_group_functionality(self):
        _add_new_group(self._course_name)

    def _create_group_buttons(self):
        for group in self._groups:
            print(group)

    def _create_button(self, group_id, row, column):
        button = tkinter.Button(self._frame, text=text, command=lambda: self._handle_button_click(group_id))
        button.grid(row=row, column=column, sticky="ew")
        
    def _handle_button_click(self, group_id):
        pass

    def start(self):
        self._create_frame()
        self._create_grid()
        self._pack()

    