from tkinter import *
import tkinter.messagebox as lil
from PIL import Image, ImageTk


def myfunc():
    print("file saved")


def help():
    print("narehs will help you")
    a = lil.showinfo("help", "need help")


def leave():
    b = lil.askyesno("leave", "wanna leave")
    if b == True:
        print("u can leave")
    else:
        print("no u cant leave")


def close():
    c = lil.askretrycancel("close", "unale to close")
    if c == True:
        print("try again")
    else:
        print("cancel please")

root = Tk()
root.title("menus and submenus")
root.geometry("400x500")
def animals():
    x = lil.askyesno("question", "which is animal")
    lil.showwarning("warning","u cant ask sillly questions")
    i = lil.askyesnocancel("question","quit app")
    if i==True:
        print("quitting")
    elif i == False:
        print("not quitting")
    else:
        print("you cancelled")
mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="open", command=myfunc)
m1.add_command(label="save", command=myfunc)
m1.add_command(label="save as", command=myfunc)
m1.add_separator()
m1.add_command(label="exit", command=myfunc)
mainmenu.add_cascade(label="file", menu=m1)
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="insert", command=myfunc)
m2.add_command(label="delete", command=myfunc)
m2.add_command(label="change", command=myfunc)
mainmenu.add_cascade(label="edit", menu=m2)
m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="help", command=help)
m3.add_command(label="leave", command=leave)
m3.add_separator()
m3.add_command(label="close", command=close)
m3.add_command(label="animal", command=animals)
mainmenu.add_cascade(label="quit", menu=m3)

root.config(menu=mainmenu)

root.mainloop()
