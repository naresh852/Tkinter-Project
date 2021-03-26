from tkinter import *
from PIL import Image,ImageTk
def attack(event):

    root.geometry(f"{width.get()}x{height.get()}")
root=Tk()
root.title("window resize")
root.geometry("900x700")
width=IntVar()
height=IntVar()
width_entry=Entry(root,textvariable=width)
height_entry=Entry(root,textvariable=height)
width_entry.pack()
height_entry.pack()
resize=Button(root,text="apply")
resize.pack()
resize.bind('<Button-1>',attack)
root.mainloop()