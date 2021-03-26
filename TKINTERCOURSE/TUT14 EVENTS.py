from tkinter import *
from PIL import Image,ImageTk
root =Tk()
def hello(event):
    print(f"u touched click me at {event.x},{event.y}")
def sizes(event):
    root.geometry("900x800")
root.title("events")
root.geometry("500x400")
widget=Button(root,text="click me")
widget.pack()
widget.bind('<Motion>',hello)
widget.bind('<Leave>',sizes)
root.mainloop()