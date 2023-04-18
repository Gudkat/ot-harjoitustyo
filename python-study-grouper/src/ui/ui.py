# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code, and also in assistance with tkinter syntax

import create_login_view as login_view
import create_guest_view as create_guest_view

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._current_view = login_view.LoginView(self._root, handle_login_button=None, handle_guest_button=self._show_guest_view)
        self._current_view.start()
    
    def render(self):
        self._current_view.render()

    def destroy(self):
        if self._current_view:
            self._current_view.destroy()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = login_view.LoginView(self._root,handle_login_button=None ,handle_guest_button=self._show_guest_view)
        self._current_view.start()

    def _show_guest_view(self):
        self._hide_current_view()
        self._current_view = create_guest_view.FindGroupView(self._root, back_button_functionality=self._show_login_view)
        self._current_view.start()

    def _handle_course_addition(self):
        self._hide_current_view()
        pass


if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    ui = UI(root)
    ui.start()
    ui.render()