from tkinter import *
root=Tk()
root.geometry("500x600")
def getval():
    print(f"name is {userval.get()}")
    print(f"pass is {passval.get()}")
user=Label(root,text="username")
paswrd=Label(root,text="pasword")
user.grid()
paswrd.grid(row=1)
# variables classes in tkinter
# Stringvar,Intvar,Booleanvar,Doublevar
userval=StringVar()
passval=StringVar()
userentry=Entry(root,textvariable=userval)
passentry=Entry(root,textvariable=passval)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(root,text="submit",command=getval).grid()
root.mainloop()
