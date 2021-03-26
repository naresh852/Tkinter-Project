from tkinter import *
from PIL import Image,ImageTk
from tkinter import Scale
import tkinter.messagebox as lil
root=Tk()
def uploaded():
    var.set("busy..")
    label.update()
    import time
    time.sleep(2)
    var.set("Ready now")
root.title("statusbar")
root.geometry("400x500")
var=StringVar()
color=StringVar()
color.set("yellow")
var.set("Ready")
label=Label(root,textvariable=var,relief=GROOVE,anchor="w",bg=color.get())
label.pack(side=BOTTOM,fill="x")
Button(root,text="upload",bg="white",command=uploaded).pack()
root.mainloop()