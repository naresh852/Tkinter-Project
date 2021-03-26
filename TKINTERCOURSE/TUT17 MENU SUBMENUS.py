from tkinter import *
from PIL import Image,ImageTk
def myfunc():
    print("file saved")
root=Tk()
root.title("menus and submenus")
root.geometry("400x500")
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="open",command=myfunc)
m1.add_command(label="save",command=myfunc)
m1.add_command(label="save as",command=myfunc)
m1.add_separator()
m1.add_command(label="exit",command=myfunc)
mainmenu.add_cascade(label="file",menu=m1)
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="insert",command=myfunc)
m2.add_command(label="delete",command=myfunc)
m2.add_command(label="change",command=myfunc)

mainmenu.add_cascade(label="edit",menu=m2)

root.config(menu=mainmenu)

root.mainloop()