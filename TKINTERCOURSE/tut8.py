from tkinter import *
root=Tk()
root.geometry("600x500")
f1=Frame(root,background="black",borderwidth=5)
f1.pack(side=LEFT,anchor="nw",fill="y")
l1=Label(f1,text="menu here")
l1.pack()
f2=Frame(root,background="lightblue",borderwidth=4)
f2.pack(fill="x",side=TOP)
l2=Label(f2,text="Welcome to pycharm")
l2.pack()
Frame(root, background="red", borderwidth=20).pack(fill="y",side=RIGHT,anchor="ne")
root.mainloop()