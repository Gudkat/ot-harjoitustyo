import initialize_database
from tkinter import Tk
from ui.ui import UI


def main():
    initialize_database.initialize_database()
    print("Database initialized")

    root = Tk()
    view = UI(root)
    view.start()
    root.mainloop()

if __name__ == "__main__":
    main()
