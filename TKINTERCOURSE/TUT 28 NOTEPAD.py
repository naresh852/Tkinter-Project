from tkinter import *
from PIL import Image,ImageTk
from tkinter import Scale
import tkinter.messagebox as mi
root=Tk()
root.title("Notepad")
root.geometry("600x400")
root.wm_iconbitmap("44.ico")
# root.configure(bg="lightblue")
text=Text(root,bg="lightblue")
text.pack()

root.mainloop()