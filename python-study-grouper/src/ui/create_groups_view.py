# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code and for checking tkinter syntax

import tkinter
from database_connection import get_connection
from database_tools.database_commands import _add_new_group, _add_to_group, _get_members_of_group, _get_ungrouped_by_course, _remove_from_group, _remove_ungrouped

class GroupsView:
    def __init__(self, root: tkinter.Tk, back_button_functionality, course_name, group_id):
        self._root = root
        self._frame = None
        self._back_button_functionality = back_button_functionality
        self._course_name = course_name
        self._group_id = group_id
        self._initialize()

    def _initialize(self):
        self._root.title(f"Study grouper - Groups for {self._course_name} Course")

    def destroy(self):
        self._frame.destroy()
        self._frame = None
    
    def start(self):
        self._create_frame()
        self._create_grid()
        self._pack()

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

    def _handle_back_button(self):
        self._back_button_functionality(self._course_name)

    def _create_frame(self):
        if self._frame:
            self.destroy()
        self._frame= tkinter.Frame(self._root, borderwidth=2, padx=20, pady=20)

    def _pack(self):
        self._frame.pack(fill="both", expand=True, side="top")

    def _create_grid(self):
        conn = get_connection()
        self._create_title_for_existing_members()
        self._create_back_button()
        self._create_rows_for_existing_members(conn)
        self._create_title_for_ungrouped_members()
        self._create_rows_for_ungrouped_members(conn)
        self._pack()

    def _create_title_for_existing_members(self):
        title = tkinter.Label(self._frame, text=f"Members of group:", font=('Arial', 16))
        title.grid(row=1, column=0, sticky="new", columnspan=2)

    def _create_rows_for_existing_members(self, conn):
        members = _get_members_of_group(conn, self._group_id)
        self._last_row = self._frame.grid_size()[1]
        print(members)
        for member in members:
            current_row = self._last_row + 1
            self._create_label(current_row, email=member[2])
            print(member[0])
            self._create_remove_button(conn=conn, row=current_row, member_id=member[0], text="Remove from group")
            self._last_row += 1

    def _create_rows_for_ungrouped_members(self, conn):
        ungrouped = _get_ungrouped_by_course(conn, self._course_name)
        for ungrouped_member in ungrouped:
            current_row = self._last_row + 1
            self._create_label(current_row, email=ungrouped_member[1])
            self._create_add_button(conn=conn, row=current_row, ungrouped_id=ungrouped_member[0], email=ungrouped_member[1])
            self._last_row += 1

    def _create_label(self, row, email):
        label = tkinter.Label(self._frame, text=f"{email}")
        label.grid(row=row, column=0, sticky="w")

    def _create_add_button(self, conn, row, ungrouped_id, email):
        button = tkinter.Button(self._frame, text="Add to group", command=lambda: self._handle_add_button(conn, ungrouped_id, email=email))
        button.grid(row=row, column=1, sticky="e")

    def _handle_add_button(self, conn, ungrouped_id, email):
        _remove_ungrouped(conn, ungrouped_id)
        _add_to_group(conn, self._group_id, email)
        self.start()

    def _create_remove_button(self, conn, row, member_id, text):
        button = tkinter.Button(self._frame, text=text, command=lambda: self._remove_from_group_functionality(conn, member_id))
        button.grid(row=row, column=1, sticky="e")

    def _add_to_group_functionality(self, conn, group_id, member_id):
        _add_to_group(conn, group_id, member_id)

    def _remove_from_group_functionality(self, conn, member_id):
        _remove_from_group(conn, member_id)
        self.start

    def _create_title_for_ungrouped_members(self):
        title = tkinter.Label(self._frame, text=f"Ungrouped members:", font=('Arial', 16))
        title.grid(column=0, sticky="new", columnspan=2)
        self._last_row = title.grid_info()["row"]

    def _create_add_new_group_button(self):
        button = tkinter.Button(self._frame, text="Add new group", command=lambda: self._add_new_group_functionality())
        button.grid(row=0, column=1, sticky="ew")

    def _add_new_group_functionality(self):
        _add_new_group(self._course_name)

    def start(self):
        self._create_frame()
        self._create_grid()
        self._pack()

    