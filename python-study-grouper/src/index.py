from tkinter import Tk
from ui.ui import UI

def main():
    root = Tk()
    view = UI(root)
    view.start()
    root.mainloop()

if __name__ == "__main__":
    main()
