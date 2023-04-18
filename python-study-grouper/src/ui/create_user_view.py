# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code and for checking tkinter syntax

import tkinter
from os import path as os_path
from sys import path as sys_path

# importing modules is hard. Gotta go ask for help in ws to make this cleaner
new_path = os_path.dirname((__file__)) + "/../"
sys_path.append(new_path)

from database_connection import get_connection
from database_tools.database_commands import get_ungrouped


class UserView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()

    def _initialize(self):
        self._root.title("Study grouper - Logged in")
        self._root.geometry("400x400")

    def render(self):
        self._root.mainloop()

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
        self._frame= tkinter.Frame(self._root)
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)
        self._frame.grid(row=0, column=0, sticky="nsew")
        self._frame.grid_columnconfigure(0, weight=1, minsize=300)


    def _pack(self):
        self._frame.pack()

    def _create_button(self, text, row):
        button = tkinter.Button(self._frame, text=text, command=self._get_button_id)
        button.grid(row=row, sticky="nsew")

    def _create_grid(self):
        ungrouped = self._get_ungrouped()
        self._frame.columnconfigure(tuple(range(len(ungrouped))), weight=1)
        self._frame.rowconfigure(tuple(range(len(ungrouped))), weight=1)
        for entry in ungrouped:
            self._button_id = entry[0]
            self._create_button(f"{entry[1]} {entry[2]}", entry[0]-1)

    def _get_ungrouped(self):
        conn = get_connection()
        ungrouped = get_ungrouped(conn)
        return ungrouped

    def _get_button_id(self, button):
        info = button.grid_info()
        row = info['row']
        print()


def test():
    root = tkinter.Tk()
    view = UserView(root)
    # view.start()
    # view.render()
    # view._create_frame()
    # view._create_grid()
    # view._create_button("test", 0)
    # view._frame.rowconfigure(0, weight=1)
    # view._frame.columnconfigure(0, weight=1)
    # view._frame.grid(row=0, column=0, sticky="nsew")
    button = tkinter.Button(view._root, text="test")
    button.grid(row=0, column=0, sticky="nsew")
    root.mainloop()


def run():
    root = tkinter.Tk()
    view = UserView(root)
    view.start()
    view.render()

if __name__ == "__main__":
    run()