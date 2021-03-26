from tkinter import *
from PIL import Image,ImageTk
from tkinter import Scale
import tkinter.messagebox as lil
root=Tk()
root.title("note")
root.geometry("400x500")
# to add icon to application
root.wm_iconbitmap("4.ico")
# to make changes in middle
root.configure(bg="red")
# laptop screen width and height
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
print(str(width)+"x"+str(height))
print(f"{width}x{height}")
Button(text="close",bg="yellow",command=root.quit).pack()
root.mainloop()