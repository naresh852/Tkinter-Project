from tkinter import *
from PIL import Image,ImageTk
from tkinter import Scale
import tkinter.messagebox as ms
root=Tk()
def select():
    global i
    box.insert(ACTIVE,f"{i}")
    i=i+1

i=0
root.title("list boxes")
root.geometry("400x500")
box=Listbox(root)
box.pack()
box.insert(END,"what is u want")
box.insert(END,"what is they want")
Button(root,text="select this",command=select).pack()
root.mainloop()