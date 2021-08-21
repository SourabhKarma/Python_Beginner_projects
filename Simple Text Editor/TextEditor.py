from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext

root = Tk(className="Simple Text Editor")
textpad = scrolledtext.ScrolledText(root, width=700, height=700)


def open_command():
    file = filedialog.askopenfile(
        parent=root, mode="rb", title="Select a file")
    if file != None:
        contents = file.read()
        textpad.insert("1.0", contents)
        file.close()


def save_command():
    file = filedialog.asksaveasfile(mode="w")
    if file != None:
        data = textpad.get("1.0", END+"-1c")
        file.write(data)


def exit_command():
    if messagebox.askokcancel("Do you Want to QUIT :("):
        root.destroy()


def about_command():
    label = messagebox.showinfo(
        "Why are you reading this are you not sure what i am.A simple text editor for python thats what i am ;)")


def work():
    print(" I am Alive :/")


def res():
    print("Window Resized")
    root.geometry("200x100")


def norm():
    print("Window back to normal")
    root.geometry("700x700")


menu_1 = Menu(root)
root.config(menu=menu_1)


# First menu

file_menu = Menu(menu_1)
menu_1.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New File", command=work)
file_menu.add_command(label="Open", command=open_command)
file_menu.add_command(label="Save", command=save_command)
file_menu.add_command(label="Exit", command=exit_command)


# Second Menu

edit_menu = Menu(menu_1)
menu_1.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Resize", command=res)
edit_menu.add_command(label="Normal", command=norm)
edit_menu.add_cascade(label="Cut")
edit_menu.add_cascade(label="Copy")
edit_menu.add_cascade(label="Paste")
edit_menu.add_cascade(label="Paste")

# Third Menu

view_menu = Menu(menu_1)
menu_1.add_cascade(label="View", menu=view_menu)

view_menu.add_command(label="About", command=about_command)

# Forth Menu

code_menu = Menu(menu_1)
menu_1.add_cascade(label="Code", menu=code_menu)

# Fifth Menu

run_menu = Menu(menu_1)
menu_1.add_cascade(label="Run", menu=run_menu)

# Sixth Menu

help_menu = Menu(menu_1)
menu_1.add_cascade(label="Help", menu=help_menu)

# Add status bar

status = Label(root, text="Running...", bg="blue",
               relief=SUNKEN, bd=1)

textpad.pack()
root.mainloop()
