from tkinter import *

root = Tk()
root.geometry("900x600")
root.title("First scrollbar")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
text = Text(root,yscrollcommand = scrollbar.set,font="lucida 13 italic",height=100,fg="brown")
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)
root.mainloop()
exit()
from tkinter import *
from PIL import Image,ImageTk
from tkinter import Scale
import tkinter.messagebox as lil
root=Tk()
root.title("scroll bar tutorial")
root.geometry("500x600")
# create scroll bar
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
# listbox=Listbox(root,yscrollcommand=scrollbar.set)
# for i in range(300):
#     listbox.insert(END,f"item{i}")
# listbox.pack(fill=BOTH,padx=10)
label=Label(root,text="hello",yscrollcommand=scrollbar.set)
# for i in range(300):
#     Label(root,text="hello").pack()
scrollbar.config(command=label.yview)
root.mainloop()
