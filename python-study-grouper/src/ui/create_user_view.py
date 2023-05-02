# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code and for checking tkinter syntax

import tkinter
from database_connection import get_connection
from database_tools.database_commands import _get_ungrouped, _remove_ungrouped

class UserView:
    def __init__(self, root: tkinter.Tk):
        self._root = root
        self._frame = None
        self._initialize()

    def _initialize(self):
        self._root.title("Study grouper - Logged in")

    def render(self):
        self._root.mainloop()

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

    def _create_ungrouped_buttons(self, ungrouped):
        for i in range(len(ungrouped)):
            self._create_button(f"{ungrouped[i][1]} {ungrouped[i][2]}", row=i, column=0, sql_id = ungrouped[i][0])

    def _create_delete_buttons(self, ungrouped):
        for i in range(len(ungrouped)):
            self._create_button("X", row=i, column=1, sql_id=ungrouped[i][0])

    def _create_button(self, text, row, column, sql_id):
        button = tkinter.Button(self._frame, text=text, command=lambda: self._handle_button_click(sql_id, column))
        button.grid(row=row, column=column, sticky="ew")

    def _create_grid(self):
        ungrouped = self._get_ungrouped()
        self._create_ungrouped_buttons(ungrouped)
        self._create_delete_buttons(ungrouped)
        self._frame.columnconfigure(0, weight=1)

    def _get_ungrouped(self):
        conn = get_connection()
        ungrouped = _get_ungrouped(conn)
        return ungrouped
    
    def _remove_ungrouped(self, id):
        conn = get_connection()
        _remove_ungrouped(conn, id)

    def _handle_button_click(self, sql_id, column):
        print("sql_id:", sql_id, "column:", column)
        if column == 1:
            self._remove_ungrouped(sql_id)
            self._create_frame()
            self._create_grid()
            self._pack()

def run():
    root = tkinter.Tk()
    view = UserView(root)
    view.start()
    view.render()

if __name__ == "__main__":
    run()