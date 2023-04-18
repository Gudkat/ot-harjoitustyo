# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code and for checking tkinter syntax

import tkinter
from os import path as os_path
from sys import path as sys_path
from dotenv import load_dotenv

# importing modules is hard. Gotta go ask for help in ws to make this cleaner
new_path = os_path.dirname((__file__)) + "/../"
sys_path.append(new_path)

from database_connection import get_connection

class LoginView:
    def __init__(self, root, handle_login_button, handle_guest_button):
        self._root = root
        self._frame = None
        self._handle_login_button = handle_login_button
        self._handle_guest_button = handle_guest_button
        self._initialize()

    def _initialize(self):
        self._root.title("Study grouper - Login")
        self._root.geometry("400x400")

    def render(self):
        self._root.mainloop()

    def destroy(self):
        self._frame.destroy()
        self._frame = None

    def start(self):
        self._create_frame()
        self._create_guest_button()
        self._create_grid()
        self._pack()

    def _create_frame(self):
        if self._frame:
            self.destroy()
        self._frame= tkinter.Frame(self._root, padx=20, pady=20)

    def _pack(self):
        self._frame.pack()

    def _create_grid(self):
        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_columnconfigure(1, weight=1)
        self._create_label("User name", 1)
        self._create_label("Password", 2)
        self._create_username_textbox()
        self._create_password_textbox()
        self._create_login_button()

    def _create_login_button(self):
        button = tkinter.Button(self._frame, text="Login", command=self._get_login_info)
        button.grid(row=4, sticky="ew", columnspan=2, pady=20)

    def _create_guest_button(self):
        button = tkinter.Button(self._frame, text="Sign up for a group", height=14, command=self._guest_login)
        button.grid(pady=(2,15))
        button.grid(row=0, column=0, columnspan=2, sticky="ew")

    def _guest_login(self):
        print("Guest login")
        self._handle_guest_button()

    def _get_login_info(self):
        print(self._username_tb.get(), self._pass_tb.get())

    def _create_username_textbox(self):
        self._username_tb = tkinter.Entry(self._frame)
        self._username_tb.grid(row=1, column=1, sticky="ew")

    def _create_password_textbox(self):
        self._pass_tb = tkinter.Entry(self._frame, show="*")
        self._pass_tb.grid(row=2, column=1, sticky="ew")

    def _create_label(self, text, row):
        label = tkinter.Label(self._frame, text=text)
        label.grid(row=row, column=0, sticky="w", padx=20, pady=1)


def run():
    root = tkinter.Tk()
    view = LoginView(root, lambda: print("Login"), lambda: print("Guest"))
    view.start()
    view.render()


if __name__ == "__main__":
    run()