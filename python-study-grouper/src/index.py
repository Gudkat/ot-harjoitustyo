import initialize_database
from tkinter import Tk
from ui.ui import UI


def main():
    initialize_database.initialize_database()
    print("Database initialized")

    # I'll fix UI to run through here for next week, but importing was confusing. Got some help from workshop but
    # no time to fix it yet. 

    # root = Tk()
    # view = UI(root)
    # view.start()

    # root.mainloop()

if __name__ == "__main__":
    main()
