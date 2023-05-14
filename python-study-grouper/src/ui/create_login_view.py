# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code and for checking tkinter syntax

import tkinter
from config import ADMIN_USERNAME, ADMIN_PASSWORD
from database_tools.database_commands import _initialize_database

class LoginView:
    def __init__(self, root, handle_succesful_login, handle_guest_button):
        self._root = root
        self._frame = None
        self._handle_succesful_login = handle_succesful_login
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
        self._create_initial_database_button()

    def _create_login_button(self):
        button = tkinter.Button(self._frame, text="Login", command=self._get_login_info)
        button.grid(row=4, sticky="ew", columnspan=2, pady=20)

    def _create_guest_button(self):
        button = tkinter.Button(self._frame, text="Sign up for a group", height=10, command=self._guest_login)
        button.grid(pady=(2,15))
        button.grid(row=0, column=0, columnspan=2, sticky="ew")

    def _guest_login(self):
        self._handle_guest_button()

    def _get_login_info(self):
        if self._username_tb.get() == ADMIN_USERNAME and self._pass_tb.get() == ADMIN_PASSWORD:
            print("Login succesful")
            self._handle_succesful_login()
        else:
            print("Wrong username or password")

    def _create_username_textbox(self):
        self._username_tb = tkinter.Entry(self._frame)
        self._username_tb.grid(row=1, column=1, sticky="ew")

    def _create_password_textbox(self):
        self._pass_tb = tkinter.Entry(self._frame, show="*")
        self._pass_tb.grid(row=2, column=1, sticky="ew")

    def _create_label(self, text, row):
        label = tkinter.Label(self._frame, text=text)
        label.grid(row=row, column=0, sticky="w", padx=20, pady=1)

    def _create_initial_database_button(self):
        button = tkinter.Button(
            self._frame, 
            text="initialize database", 
            command=_initialize_database
        )
        button.grid(columnspan=2)