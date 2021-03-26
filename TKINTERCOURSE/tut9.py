from tkinter import *
root=Tk()
root.geometry("600x500")
def first():
    print("first button")
def second():
    print("second button")
def third():
    print("third button")
def fourth():
    print("fourth button")
f1=Frame(root,bg="yellow",bd=10)
f1.pack(fill="x")
f2=Frame(f1,bg="yellow",bd=5)
f2.pack(side=TOP)
b1=Button(f2,fg="black",bg="skyblue",text="print first",command=first)
b1.pack(side=LEFT,padx="10")
b2=Button(f2,fg="black",bg="skyblue",text="print second",command=second)
b2.pack(side=LEFT,padx="10")
b3=Button(f2,fg="black",bg="skyblue",text="print third",command=third)
b3.pack(side=LEFT,padx="10")
b4=Button(f2,fg="black",bg="skyblue",text="print fourth",command=fourth)
b4.pack(side=LEFT,padx="10")
root.mainloop()