from tkinter import *


class MainMenu:

    def __init__(self, master):
        self.frame = Frame(master, height=300, width=300)
        self.frame.pack()

        self.root_menu = Menu(master)
        self.file_menuitem = Menu(self.root_menu, tearoff=0)  # tearoff hides the default ----- option.
        self.edit_menuitem = Menu(self.root_menu, tearoff=0)  # tearoff hides the default ----- option.
        self.view_menuitem = Menu(self.root_menu, tearoff=0)  # tearoff hides the default ----- option.

        master.config(menu=self.root_menu)
        self.root_menu.add_cascade(label="File", menu=self.file_menuitem)
        self.root_menu.add_cascade(label="Edit", menu=self.edit_menuitem)
        self.root_menu.add_cascade(label="View", menu=self.view_menuitem)

        self.file_menuitem.add_command(label="New Project", command=self.do_nothing)
        self.file_menuitem.add_command(label="Open Project", command=self.do_nothing)
        self.file_menuitem.add_separator()
        self.file_menuitem.add_command(label="Exit", command=self.frame.quit)

        self.edit_menuitem.add_command(label="Cut", command=self.do_nothing)
        self.edit_menuitem.add_command(label="Copy", command=self.do_nothing)
        self.edit_menuitem.add_command(label="Paste", command=self.do_nothing)

        self.view_menuitem.add_command(label="Tool Windows", command=self.do_nothing)
        self.view_menuitem.add_command(label="Cascade Windows", command=self.do_nothing)
        self.view_menuitem.add_command(label="Save Layout", command=self.do_nothing)

    def do_nothing(self):
        print("Doing nothing")


if __name__ == "__main__":
    root = Tk()
    example_window = MainMenu(root)
    root.mainloop()

