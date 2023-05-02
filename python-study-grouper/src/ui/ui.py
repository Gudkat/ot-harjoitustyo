# git copilot has been used in creation of this file
# ChatGPT has been used to debug the code, and also in assistance with tkinter syntax

from ui.create_login_view import LoginView
from ui.create_guest_view import FindGroupView
from ui.create_user_view import UserView
from ui.create_overview_view import OverviewView
from ui.create_add_to_group_view import AddToGroupView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()
        self._current_view.start()

    def destroy(self):
        if self._current_view:
            self._current_view.destroy()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root,handle_succesful_login=self._show_overview_view ,handle_guest_button=self._show_guest_view)
        self._current_view.start()

    def _show_guest_view(self):
        self._hide_current_view()
        self._current_view = FindGroupView(self._root, back_button_functionality=self._show_login_view)
        self._current_view.start()

    def _show_user_view(self):
        self._hide_current_view()
        self._current_view = UserView(self._root)
        self._current_view.start()

    def _show_overview_view(self):
        self._hide_current_view()
        self._current_view = OverviewView(
            self._root, 
            back_button_functionality=self._show_login_view, 
            add_to_group_button_functionality=self._show_add_to_group_view
            )
        self._current_view.start()

    def _show_add_to_group_view(self, course_name):
        self._hide_current_view()
        self._current_view = AddToGroupView(
            self._root, 
            course_name, 
            back_button_functionality=self._show_overview_view, 
            add_button_functionality=self._show_ungrouped_for_specific_group_view
            )
        self._current_view.start()

    def _show_ungrouped_for_specific_group_view(self, course_name, group_id):
        self._hide_current_view()
        pass

    def _handle_course_addition(self):
        self._hide_current_view()
